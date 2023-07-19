from PIL import Image
from woocommerce import API
import math, time, random, requests, os, customtkinter, json


wcapi = API(
    url="", #URL de tu tienda
    consumer_key="",
    consumer_secret="",
    version="wc/v3",
)

ig_user_id = "" #el user ID que te da la app de facebook developer


# Si este programa te ha sido de utilidad no olvides
# SUSCRIBIRTE a mi canal de YOUTUBE 👇👇👇
# https://www.youtube.com/@codeffee_ ☕


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        def api_key():
            key = self.api_key_entry.get()
            with open("key.json", "w") as outfile:json.dump(key, outfile)

        def obtenerDatos():
            residuo = 0
            numDePaginas = 0
            productos = []
            whilekey = False
            while whilekey == False:
                try:
                    totalProductos = (
                        wcapi.get("reports/products/totals").json()[2]["total"]
                        + wcapi.get("reports/products/totals").json()[3]["total"]
                    )
                    whilekey = True
                except:
                    self.label4.configure(text="Reconectando con el servidor...")
                    time.sleep(5)
            residuo = totalProductos % 100
            numDePaginas = totalProductos / 100
            if residuo == 0:
                for i in range(1, numDePaginas + 1):
                    whilekey = False
                    while whilekey == False:
                        try:
                            productos.append(
                                wcapi.get(
                                    "products",
                                    params={
                                        "per_page": 100,
                                        "stock_status": "instock",
                                        "page": (i),
                                    },
                                ).json()
                            )
                            whilekey = True
                            t = time.localtime()
                            current_time = time.strftime("%H:%M:%S", t)
                            self.label4.configure(
                                text="Base de datos descargada con éxito! %s"
                                % (str(current_time))
                            )
                        except:
                            self.label4.configure(
                                text="Reconectando con el servidor..."
                            )
                            time.sleep(5)
            else:
                numDePaginas = math.ceil(numDePaginas)
                for i in range(1, numDePaginas + 1):
                    whilekey = False
                    while whilekey == False:
                        try:
                            productos.append(
                                wcapi.get(
                                    "products",
                                    params={
                                        "per_page": 100,
                                        "stock_status": "instock",
                                        "page": (i),
                                    },
                                ).json()
                            )
                            whilekey = True
                            t = time.localtime()
                            current_time = time.strftime("%H:%M:%S", t)
                            self.label4.configure(
                                text="Base de datos descargada con éxito! %s"
                                % (str(current_time))
                            )
                        except:
                            self.label4.configure(
                                text="Reconectando con el servidor..."
                            )
                            time.sleep(5)
            productosSeleccionados = []
            for i in range(len(productos)):
                for j in range(len(productos[i])):
                    productosSeleccionados.append(
                        [
                            productos[(i)][j]["name"],
                            productos[(i)][j]["images"][0]["src"],
                            productos[(i)][j]["images"][0]["alt"]
                        ]
                    )
            with open("data.json", "w") as outfile:json.dump(productosSeleccionados, outfile)

        def publicar():
            with open('data.json', 'r') as openfile:
                # Reading from json file
                data = json.load(openfile)
            numero = random.randrange(0, len(data), 1)
            with open('key.json', 'r') as openfile:
                # Reading from json file
                access_token = json.load(openfile)
            image_url = data[numero][1]
            frase = data[numero][2]
            caption = (
                frase + "\nHaz tus pedidos por DM 🛒🔥\nMás productos en nuestra tienda online\n.\n.\nContamos con envío a domicilio\n📩Pedidos por DM\n🛒 o en nuestra tienda online (link en BIO)\n#tiendaenlinea #woocommerce @codeffee_"
            )
            post_url = "https://graph.facebook.com/v15.0/%s/media" % (ig_user_id)
            param = dict()
            param["access_token"] = access_token
            param["caption"] = caption
            param["image_url"] = image_url
            try:
                response = requests.post(post_url, params=param)
                response = response.json()

                if "id" in response:
                    creation_id = response["id"]
                    second_url = "https://graph.facebook.com/v15.0/%s/media_publish" % (
                        ig_user_id
                    )
                    second_param = dict()
                    second_param = {
                        "access_token": access_token,
                        "creation_id": creation_id,
                    }
                    response = requests.post(second_url, params=second_param)
                    response = response.json()
                    t = time.localtime()
                    current_time = time.strftime("%H:%M:%S", t)
                    self.label4.configure(text="Imagen publicada! %s" % (str(current_time)))
                else:
                    t = time.localtime()
                    current_time = time.strftime("%H:%M:%S", t)
                    self.label4.configure(
                        text="Error: No fue posible publicar %s" % (str(current_time))
                    )
            except:
                self.label4.configure(
                        text="Error: Error de conexión %s" % (str(current_time))
                    )

        self.title("Publicaciones Automáticas")
        self.geometry("700x450")
        self.resizable(False, False)

        # set grid layout 1x2
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # load images with light and dark mode image
        image_path = os.path.join(
            os.path.dirname(os.path.realpath(__file__)), "test_images"
        )
        self.logo_image = customtkinter.CTkImage(
            Image.open(os.path.join(image_path, "CustomTkinter_logo_single.png")),
            size=(26, 26),
        )
        self.large_test_image = customtkinter.CTkImage(
            Image.open(os.path.join(image_path, "large_test_image.png")),
            size=(500, 150),
        )
        self.image_icon_image = customtkinter.CTkImage(
            Image.open(os.path.join(image_path, "image_icon_light.png")), size=(20, 20)
        )
        self.image_icon_image2 = customtkinter.CTkImage(
            Image.open(os.path.join(image_path, "image_icon_light-des.png")),
            size=(20, 20),
        )
        self.image_icon_image3 = customtkinter.CTkImage(
            Image.open(os.path.join(image_path, "image_icon_light-ins.png")),
            size=(20, 20),
        )
        self.home_image = customtkinter.CTkImage(
            light_image=Image.open(os.path.join(image_path, "home_dark.png")),
            dark_image=Image.open(os.path.join(image_path, "home_light.png")),
            size=(20, 20),
        )
        self.chat_image = customtkinter.CTkImage(
            light_image=Image.open(os.path.join(image_path, "chat_dark.png")),
            dark_image=Image.open(os.path.join(image_path, "chat_light.png")),
            size=(20, 20),
        )
        self.add_user_image = customtkinter.CTkImage(
            light_image=Image.open(os.path.join(image_path, "add_user_dark.png")),
            dark_image=Image.open(os.path.join(image_path, "add_user_light.png")),
            size=(20, 20),
        )

        # create navigation frame
        self.navigation_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(4, weight=1)

        self.navigation_frame_label = customtkinter.CTkLabel(
            self.navigation_frame,
            text="  Publicaciones Automáticas",
            image=self.logo_image,
            compound="left",
            font=customtkinter.CTkFont(size=15, weight="bold"),
        )
        self.navigation_frame_label.grid(row=0, column=0, padx=20, pady=20)

        self.home_button = customtkinter.CTkButton(
            self.navigation_frame,
            corner_radius=0,
            height=40,
            border_spacing=10,
            text="Mi tienda",
            fg_color="transparent",
            text_color=("gray10", "gray90"),
            hover_color=("gray70", "gray30"),
            image=self.home_image,
            anchor="w",
            command=self.home_button_event,
        )
        self.home_button.grid(row=1, column=0, sticky="ew")

        self.appearance_mode_menu = customtkinter.CTkOptionMenu(
            self.navigation_frame,
            values=["Light", "Dark", "System"],
            command=self.change_appearance_mode_event,
        )
        self.appearance_mode_menu.grid(row=6, column=0, padx=20, pady=20, sticky="s")

        # create home frame
        self.home_frame = customtkinter.CTkFrame(
            self, corner_radius=0, fg_color="transparent"
        )
        self.home_frame.grid_columnconfigure(0, weight=1)

        self.home_frame_large_image_label = customtkinter.CTkLabel(
            self.home_frame, text="", image=self.large_test_image
        )
        self.home_frame_large_image_label.grid(
            row=0, column=0, columnspan=2, padx=20, pady=10
        )

        self.api_key_entry = customtkinter.CTkEntry(
            self.home_frame, placeholder_text="Instagram API KEY", width=300
        )
        self.api_key_entry.grid(row=1, column=0, padx=20, pady=(25, 35))
        self.home_frame_button_2 = customtkinter.CTkButton(
            self.home_frame,
            text="Renovar",
            image=self.image_icon_image,
            compound="right",
            command=api_key,
        )
        self.home_frame_button_2.grid(row=1, column=1, padx=20, pady=(25, 35))

        self.label1 = customtkinter.CTkLabel(
            self.home_frame, text="Actualizar base de datos", fg_color="transparent"
        )
        self.label1.grid(row=3, column=0, padx=20, pady=2)
        self.label2 = customtkinter.CTkLabel(
            self.home_frame, text="Publicar producto", fg_color="transparent"
        )
        self.label2.grid(row=3, column=1, padx=20, pady=2)

        self.home_frame_button_1 = customtkinter.CTkButton(
            self.home_frame,
            text="Descargar productos",
            image=self.image_icon_image2,
            compound="right",
            width=300,
            command=obtenerDatos,
        )
        self.home_frame_button_1.grid(row=4, column=0, padx=20, pady=2)
        self.home_frame_button_3 = customtkinter.CTkButton(
            self.home_frame,
            text="Publicar",
            image=self.image_icon_image3,
            compound="right",
            command=publicar,
        )
        self.home_frame_button_3.grid(row=4, column=1, padx=20, pady=2)

        self.label3 = customtkinter.CTkLabel(
            self.home_frame,
            text="",
            fg_color="transparent",
        )
        self.label3.grid(row=5, column=0, padx=20, pady=(10, 35), columnspan=2)
        self.label4 = customtkinter.CTkLabel(
            self.home_frame, text="", corner_radius=22, text_color="cyan"
        )
        self.label4.grid(row=6, column=0, padx=20, pady=2, columnspan=2)


        # select default frame
        self.select_frame_by_name("home")

    def select_frame_by_name(self, name):
        # set button color for selected button
        self.home_button.configure(
            fg_color=("gray75", "gray25") if name == "home" else "transparent"
        )

        # show selected frame
        if name == "home":
            self.home_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.home_frame.grid_forget()

    def home_button_event(self):
        self.select_frame_by_name("home")

    def change_appearance_mode_event(self, new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)


if __name__ == "__main__":
    app = App()
    app.mainloop()
