:
            e += 1
            tk.Label(master=display_scheduled, text=("-----", a)).grid(row=e, column=0)
        e += 1
        tk.Label(master=display_scheduled, text="Standard Users Are:").grid(row=e, column=0)
        for a in standard:
            e += 1
            tk.Label(master=display_scheduled, text=("-----", a)).grid(row=e, column=0)

    def deleting_users():
        def deleting_back_user():
            user = username.get()
            if not (user in admin or user in manager or user in standard):
                root = tk.Tk()
                root.title("Username Not Found!")
                tk.Label(master=root, text="Username not found! Please try again!").grid(row=1, column=1)
            else:
                if user in admin:
                    del admin[user]
                    admin1 = tk.Tk()
                    admin1.title("Success!")
                    tk.Label(master=admin1, text="Admin User Successfully Deleted!").grid(row=1, column=1)
                    delete_users_scheduled.destroy()
                elif user in manager:
                    del manager[user]
                    admin1 = tk.Tk()
                    admin1.title("Success!")
                    tk.Label(master=admin1, text=" Manager Successfully Deleted!").grid(row=1, column=1)
                    delete_users_scheduled.destroy()
                if user in standard:
                    del standard[user]
                    admin1 = tk.Tk()
                    admin1.title("Success!")
                    tk.Label(master=admin1, text="Standard User Successfully Deleted!").grid(row=1, column=1)
                    delete_users_scheduled.destroy()
