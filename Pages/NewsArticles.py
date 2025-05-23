from tkinter import*
from tkinter import ttk
import customtkinter
import requests
from sql_app.models import NewsArticle
from Components import NavBar
import pyperclip


class NewsArticles(Frame):

    def __init__(self, parent, controller, orgnumber):
        Frame.__init__(self, parent)
        self.orgnumber = orgnumber


        # Frames
        top_frame = customtkinter.CTkFrame(self,
                                height= 200, 
                                corner_radius=0,
                            )
        top_frame.grid(row = 0, column = 0, sticky = "nswe")
        
        middle_frame = customtkinter.CTkFrame(self,
                                height= 10, 
                               
                            )
        middle_frame.grid(row = 2, column = 0, sticky = "nswe", padx = 10, pady = 20)

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

        delete_new = customtkinter.CTkButton(middle_frame, text="Delete article", command= self.delete_news)
        delete_new.grid(row=1, column=3, columnspan=1, pady=10, padx=10, ipadx= 30 )


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
        self.tree.column("Title", anchor=W, width= 260)
        self.tree.column("Url", anchor=W, width= 600)
       

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

        

        self.tree.bind("<Control-Key-c>", self.copy_from_treeview)

    def copy_from_treeview(self, _):
        selections = self.tree.selection()  # get hold of selected rows

        copied_string = ""
        for row in selections:
            values = self.tree.item(row, 'values')  # get values for each selected row

            for item in values:
                copied_string += f"{item}  "

        pyperclip.copy(copied_string)


    def create_newsarticle(self):
        news_article = NewsArticle(
            Title = self.title_entry.get(),
            URL = self.url_entry.get(),
            OrgNumber = self.orgnumber
        )
        return news_article

    def saveArticle(self):
        news_article = self.create_newsarticle()
        if len(self.tree.get_children()) % 2 == 0:
            self.tree.insert(parent='', index= 'end', iid=news_article.ArticleId, text="", values=(news_article.Title, news_article.URL), tags=('evenrow'))
        else:
            self.tree.insert(parent='', index= 'end', iid=news_article.ArticleId, text="", values=(news_article.Title, news_article.URL), tags=('')) 

        URL = "http://127.0.0.1:8000/Company/" + str(self.orgnumber) + "/NewsArticle"
        DATA = {"URL": news_article.URL, "Title": news_article.Title, "OrgNumber": news_article.OrgNumber}
        requests.post(url = URL, json = DATA)

    def make_treeview(self):
        URL = "http://127.0.0.1:8000/NewsArticle/Org/" + str(self.orgnumber)
        PARAMS = {"OrgNumber": self.orgnumber}
        r = requests.get(url=URL, params=PARAMS)
        
        news_articles = r.json()

        count_color = 0
        for news_article in news_articles:
            if count_color %2 ==0:
                self.tree.insert(parent='', index= 'end', iid=news_article["ArticleId"], text="", values=(news_article["Title"],news_article["URL"]), tags=('evenrow'))
            else:
                self.tree.insert(parent='', index= 'end', iid=news_article["ArticleId"], text="", values=(news_article["Title"],news_article["URL"]), tags=(''))
        
            count_color +=1


    def delete_news(self):
        articleId = self.tree.focus()
        self.tree.delete(articleId)
        URL = "http://127.0.0.1:8000/NewsArticle/" + str(articleId) + "/delete"
        PARAMS = {"ArticleId": articleId}
        requests.delete(url = URL, params = PARAMS)