import tkinter as tk
from Cafe_Main import clientes, empleados, pedidos, buscar_usuario
from Cafe_Back import *



ventana = tk.Tk()
ventana.title("Cafe")
ventana.geometry("400x300")

usuario_actual = [None]

def mostrar_frame(frame):
    frame.tkraise()

def login():
    try:
        id = int(entrada_id.get())
        usuario = buscar_usuario(id, clientes, empleados)
        if usuario is None:
            label_error.config(text="ID no encontrado. Intenta nuevamente.")
        else:
            usuario_actual[0] = usuario
            if isinstance(usuario, Cliente):
                label_bienvenida_cliente.config(text=f"Bienvenido {usuario.name} ")
                label_puntos.config(text=f"Puntos: {usuario.puntos}")
                mostrar_frame(frame_cliente)
            else:
                label_bienvenida_empleado.config(text=f"Bienvenido {usuario.name}, {usuario.Rol}")
                mostrar_frame(frame_empleado)
    except:
        label_error.config(text="Ingresa un ID válido.")

def realizar_pedido():
    usuario_actual[0].pedir()
    usuario_actual[0].puntos += 10
    nuevo_pedido = Pedido(len(pedidos) + 1, "PENDIENTE")
    nuevo_pedido.productos.append(usuario_actual[0].historial_compras[-1])
    pedidos.append(nuevo_pedido)
    label_puntos.config(text=f"Puntos: {usuario_actual[0].puntos}")



def ver_historial():
    historial = usuario_actual[0].historial_compras
    if len(historial) == 0:
        label_info.config(text="No tienes pedidos aún.")
    else:
        texto = "".join(historial)
        label_info.config(text=f"Hisorial: {texto}")


#################################
def canjear_puntos():
    usuario_actual[0].canjear_Puntos()
    label_puntos.config(text=f"Puntos: {usuario_actual[0].puntos}")

def ver_pedidos():
    if len(pedidos) == 0:
        label_info_empleado.config(text="No hay pedidos pendientes.")
    else:
        texto = "".join([f"Pedido {p.idPedido} - {p.estado}" for p in pedidos])
        label_info_empleado.config(text=texto)

def cambiar_estado():
    if len(pedidos) == 0:
        label_info_empleado.config(text="No hay pedidos pendientes.")
    else:
        pedido = pedidos[-1]  #
        usuario_actual[0].cambiarEstadoPedido(pedido)
        label_info_empleado.config(text=f"Pedido {pedido.idPedido} ahora está: {pedido.estado}")

def cerrar_sesion():
    usuario_actual[0] = None
    entrada_id.delete(0, tk.END)
    label_error.config(text="")
    label_info.config(text="")
    mostrar_frame(frame_login)

#####ventana de id
frame_login = tk.Frame(ventana)
frame_login.place(relwidth=1, relheight=1)

tk.Label(frame_login, text="Cafetería", font=("Arial", 20, "bold")).pack(pady=20)
tk.Label(frame_login, text="Ingresa tu ID:").pack()
entrada_id = tk.Entry(frame_login, justify="center")
entrada_id.pack(pady=5)
label_error = tk.Label(frame_login, text="")
label_error.pack()
tk.Button(frame_login, text="Entrar", width=15, command=login).pack(pady=10)

####Usuario
frame_cliente = tk.Frame(ventana)
frame_cliente.place(relwidth=1, relheight=1)

label_bienvenida_cliente = tk.Label(frame_cliente, text="", font=("Arial", 13, "bold"))
label_bienvenida_cliente.pack(pady=10)
label_puntos = tk.Label(frame_cliente, text="")
label_puntos.pack()

tk.Button(frame_cliente, text="Realizar pedido", width=20, command=realizar_pedido).pack(pady=5)
tk.Button(frame_cliente, text=" Ver historial", width=20, command=ver_historial).pack(pady=5)
tk.Button(frame_cliente, text="Canjear puntos", width=20, command=canjear_puntos).pack(pady=5)
label_info = tk.Label(frame_cliente, text="", wraplength=300)
label_info.pack(pady=5)
tk.Button(frame_cliente, text="Cerrar sesión", command=cerrar_sesion).pack(pady=5)

#####Empledo
frame_empleado = tk.Frame(ventana)
frame_empleado.place(relwidth=1, relheight=1)

label_bienvenida_empleado = tk.Label(frame_empleado, text="", font=("Arial", 13, "bold"))
label_bienvenida_empleado.pack(pady=10)

tk.Button(frame_empleado, text="Vrr pedidos", width=20, command=ver_pedidos).pack(pady=5)
tk.Button(frame_empleado, text="Cambiar estado", width=20, command=cambiar_estado).pack(pady=5)
label_info_empleado = tk.Label(frame_empleado, text="", wraplength=300)
label_info_empleado.pack(pady=5)
tk.Button(frame_empleado, text="Cerrar sesión", command=cerrar_sesion).pack(pady=5)


mostrar_frame(frame_login)
ventana.mainloop()