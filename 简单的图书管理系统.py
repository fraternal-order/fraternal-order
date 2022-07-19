class BookManager:
    books=[['问天道','陈十三',30],['三国义','罗贯中',65],['西游记','吴承恩',70],['水浒传','施耐庵',85]]
    key=1
    lend_list=[]
    def menu(self):
    #显示选择菜单，根据不同的选项请用不同的方法
            print('\n***************************************')
            print('********  1. 查询所有书籍   **********')
            print('********  2. 添加书籍       **********')
            print('********  3. 借阅书籍       **********')
            print('********  4. 归还书籍       **********')
            print('********  0. 退出系统       **********')
            print('***************************************\n')
            v=int(input('请输入对应的数字：\n'))
            self.v = v
            
 
                 
             
    def show_all_book(self):
    #显示每本数据的信息
        if self.v == 1:
            print('\n书名\t\t','作者\t\t\t','价格\n')
            for i in self.books:
                print(i[0],'\t\t',i[1],'\t\t',i[2])
 
                     
    def add_book(self):
    #添加书籍
        if self.v == 2:
            bookname=input('请输入书名：')
            author=input('请输入作者：')
            price=int(input('请输入价格：'))
            self.books.append([bookname,author,price])
            print('\n添加书籍成功！')
             
    def lend_book(self):
    #借阅书籍
        if self.v == 3:
            bookname= input("请输入书籍名称：")
            author=input("请输入作者：")
            j=0
            for i in self.books:
                if i[0]==bookname:
                    if i[1] == author:
                        j=1
                        print('书名：',i[0],'作者：',i[1],'价格：',i[2])
                        price=i[2]
                        lend_person=input("请输入借阅人名字：")
                        self.lend_list.append([lend_person,bookname])
                        self.books.remove([bookname,author,price])
                        print('借阅成功:')
                if j==0:
                    print('该书籍不存在！自动返回...')
            print(self.lend_list)
            print('\n借阅结束!\n')
 
    def return_book(self):
    #归还书籍
        if self.v ==4:
            bookname=input('请输入归还书名：')
            author=input('请输入归还书名作者：')
            price=int(input('请输入价格：'))
            self.books.append([bookname,author,price])
            lend_person=input("请输入借阅人名字：")
            for i in self.lend_list:
                if i[0]==lend_person:
                    if i[1]==bookname:
                        self.lend_list.remove([lend_person,bookname])
            print(self.lend_list)
            print('\n归还书籍成功！')
             
    def main(self):
        while self.key==1:
             
            print('\n欢迎登录图书系统！')
            self.menu()
            self.show_all_book()
            self.add_book()
            self.lend_book()
            self.return_book()
            if self.v==0:
                break
        print('感谢使用图书系统！')
BM = BookManager()
BM.main()
