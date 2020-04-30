class scrapeClass:
    def __init__(self, login, password, follName, directory):
        self.login = login
        self.password = password
        self.follName = follName
        self.directory = directory
        print("__init__")

    def getFollowers(self):
        import xlsxwriter
        import instaloader
        print("btnClicked2")
        print("getFollowers")
        print("Loading..")
        self.L = instaloader.Instaloader()
        login="vling9898"
        password="gaBWwkvpV6YukQwWhgFy"
        self.L.login(login, password)
        print("Logged in..")
        self.profile = instaloader.Profile.from_username(self.L.context, self.follName)
        self.followerNames = []
        self.followeeNames=[]
        i=0
        print("Getting followees.. This might take a while")
        for followers in self.profile.get_followers():
            i+=1
            print(str(i) + ": Username: " + followers.username)
            self.followerNames.append(followers.username)

        for followees in self.profile.get_followees():
            i += 1
            print(str(i) + ": Username: " + followees.username)
            self.followeeNames.append(followees.username)

        #Write Tto xlsx
        workbook = xlsxwriter.Workbook(self.directory + '/followerNames.xlsx')
        worksheet = workbook.add_worksheet()
        worksheet.set_column('A:A', 40)
        worksheet.write('A1', "Followers of User: " + self.follName)
        worksheet.write('A2', " ")
        worksheet.write_column('A3', self.followeeNames)
        worksheet.write('B1', "Followees of User: " + self.follName)
        worksheet.write('B2', " ")
        worksheet.write_column('B3', self.followeeNames)
        workbook.close()
        print("write to " + self.directory + "/followerNames.xlsx")
        print("done")

    #Instaloader Like Function
    def get_all_likes(self,max):
        import instaloader
        print("type of max")
        print(type(max))
        self.L = instaloader.Instaloader()
        print("login")
        print("self.login " + self.login)
        self.L.login(self.login, self.password)
        profile = instaloader.Profile.from_username(self.L.context, self.follName)
        likes = set()
        i=0
        print("max " + str(max))
        self.likeCount=0
        for post in profile.get_posts():
            if(i<int(max)):
                i+=1
                print(i)
                print("post number " + str(i) + " has " + str(post.likes) + " likes")
                likes = likes | set(post.get_likes())
                self.likeCount+=post.likes
                self.likes=likes
                print(likes)

        i=0
        self.likeList = []
        for x in likes:
            i+=1
            self.likeList.append(str(i) + ": " + str(x).split()[1])
        print("Likelist:")
        print(self.likeList)
        print("Got the last Likes from the last " + str(max) + " profiles.")
        self.directory=self.directory + r"/GetLikes.xlsx"
        print("Writing to : " + self.directory)
        self.writeToXlsx(self.likeList, self.directory)


    def writeToXlsx(self, data, directory):
        print(directory)
        import xlsxwriter
        workbook = xlsxwriter.Workbook(directory)
        worksheet = workbook.add_worksheet()
        worksheet.write_column('A2', data)
        workbook.close()
#foo=scrapeClass("vling9898", "gaBWwkvpV6YukQwWhgFy", "hotelathenalignano",r"C:\downloads\names.xlsx")
#foo.get_all_likes(2)


#foo2=scrapeClass("vling9898", "gaBWwkvpV6YukQwWhgFy", "somewheretours",r"C:\downloads\names.xlsx")
#foo2.getFollowers()

#
#
# #test
# import xlsxwriter
# import instaloader
# L = instaloader.Instaloader()
# #"vling9898", "gaBWwkvpV6YukQwWhgFy"
# login="vling9898"
# password="gaBWwkvpV6YukQwWhgFy"
# L.login(login, password)
# #self.follName="andredupke"
# follName="gurunaj"
# profile = instaloader.Profile.from_username(L.context, follName)
# i=0
# temp=[]
# likes=set()
# for post in profile.get_posts():
#     likes=likes | set(post.get_likes())
# likeList=[]
# for x in likes:
#     likeList.append(str(x).split()[1])
#
#
#
#
#
#
#
#
#
#         followerNames = []
#         followeeNames=[]
#         i=0
#         for followers in profile.get_followers():
#             i+=1
#             print(str(i) + ": Username: " + followers.username)
#             followerNames.append(followers.username)
#         for followees in profile.get_followees():
#             i += 1
#             print(str(i) + ": Username: " + followees.username)
#             followeeNames.append(followees.username)
# #testende
#
#
#
