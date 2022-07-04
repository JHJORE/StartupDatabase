from tkinter import*
from tkinter import ttk
import customtkinter
import requests
from sql_app.models import NewsArticle
from Components import NavBar


class NewsArticles(Frame):

    def __init__(self, parent, controller, orgnumber):
        Frame.__init__(self, parent)
        self.orgnumber = orgnumber


        # Frames
        top_frame = customtkinter.CTkFrame(self)
        top_frame.grid(row = 0, column = 0, sticky = "nswe", padx = 20, pady = 10)
        
        middle_frame = customtkinter.CTkFrame(self,
                                height= 10, 
                                corner_radius=0,
                            )
        middle_frame.grid(row = 2, column = 0, sticky = "nswe")

        # title_frame = customtkinter.CTkFrame(self)
        # title_frame.grid(row = 1, column = 0, sticky = "nswe", padx = 20, pady = 10)

        bottom_frame = customtkinter.CTkFrame(self)
        bottom_frame.grid(row = 4, column = 0, sticky = "nswe", padx = 20, pady = 10)


        navbar = NavBar.NavBar(parent, controller, top_frame)

        self.title_entry = customtkinter.CTkEntry(middle_frame,
                                placeholder_text="Title",
                               width=180,
                               height=25,
                               border_width=2,
                               corner_radius=5)
        self.title_entry.grid(row=1, column=0,padx=10, pady=10)

        self.url_entry = customtkinter.CTkEntry(middle_frame,
                                placeholder_text="Url",
                               width=180,
                               height=25,
                               border_width=2,
                               corner_radius=5)
        self.url_entry.grid(row=1, column=1,padx=10, pady=10)

        add_news_button = customtkinter.CTkButton(middle_frame, text="Save Newsarticle", command= self.saveArticle)
        add_news_button.grid(row=1, column=2, columnspan=1, pady=10, padx=10, ipadx= 30 )


        vertical_scroll = Scrollbar(bottom_frame)
        vertical_scroll.pack(side=RIGHT, fill = Y )

        self.tree = ttk.Treeview(bottom_frame, yscrollcommand= vertical_scroll.set)
        self.tree.pack()
        vertical_scroll.config(command = self.tree.yview)

        self.tree['column'] = (
        "Title",
        "Url")
        #colums
        self.tree.column("#0", width=0, stretch=NO)
        self.tree.column("Title", anchor=W, width= 400)
        self.tree.column("Url", anchor=W, width= 700)
       

        #Headings
        self.tree.heading("#0", text= "", anchor= W)
        self.tree.heading("Title", text= "Title", anchor= W)
        self.tree.heading("Url", text= "Url", anchor= W)

        self.tree.tag_configure('oddrow',background="white")
        self.tree.tag_configure('evenrow',background="#51B087")

        self.make_treeview()

        title = customtkinter.CTkLabel(master=middle_frame,
                                    width=120,
                                    text="News Articles",
                                    height=45,
                                    corner_radius=8)
        title.grid(row =0, column= 0)


    def create_newsarticle(self):
        newsarticle = NewsArticle(
            Title = self.title_entry.get(),
            URL = self.url_entry.get(),
            OrgNumber = self.orgnumber
        )
        return newsarticle

    def saveArticle(self):
        newsArticle = self.create_newsarticle()
        URL = "http://127.0.0.1:8000/Company/" + str(self.orgnumber) + "/NewsArticle"
        PARAMS = {"OrgNumber": self.orgnumber, "NewsArticle": newsArticle}
        requests.post(url = URL, params = PARAMS)

    def make_treeview(self):
        URL = "http://127.0.0.1:8000/NewsArticle/Org/" + str(2)
        PARAMS = {"OrgNumber": 2}
        r = requests.get(url=URL, params=PARAMS)
        
        news_articles = r.json()

        count_color = 0
        for news_article in news_articles:
            if count_color %2 ==0:
                self.tree.insert(parent='', index= 'end', iid=news_article["ArticleId"], text="", values=(news_article["Title"],news_article["URL"]), tags=('evenrow'))
            else:
                self.tree.insert(parent='', index= 'end', iid=news_article["ArticleId"], text="", values=(news_article["Title"],news_article["URL"]), tags=(''))
        
            count_color +=1



