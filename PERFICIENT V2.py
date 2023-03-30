import mysql.connector as m #IMPORTS THE MYSQL CONNECTOR TO CONNECT THE PROGRAM TO THE DATABASE 
from getpass import getpass #IMPORTS GETPASS TO CONCEAL THE PASSWORD ENTERED FOR ADMIN LOGIN (WORKS ONLY ON TERMINAL)
#SLEEP MODULE HAS BEEN USED FOR ADMIN MENU
#PYGAME MODULE HAS BEEN USED AT MANY AREAS INVOLVING USER,EMPLOYEE,& ADMIN BACKEND INTERFACES
con=m.connect(host='localhost',user='root',password="Kiran@175",database='PERFICIENT')
print("SUCCESSFULLY CONNECTED")
print(con)
A=con.cursor()

def DATA():#DISPLAYS ALL DATA IN THE DATABASE
    print("DATABASE NAME: PERFICIENT")
    print("NUMBER OF TABLES: 9")
    S1="SHOW TABLES"
    A.execute(S1)
    f1=A.fetchall()
    print("TABLES:")
    print("_______________")
    for i in f1:
        for j in i:
            print(j)
            print("________________")
    print("")
    print("PRODUCTS ON SALE: ")
    A.execute("SELECT * from CATALOGE")
    Q=A.fetchall()
    for i in Q:
        print("PRODUCT_ID:",i[0])
        print("PRICE:",i[1])
        print("PRODUCT NAME:",i[2])
        print("________________________________________________________________________________")
    print("")
    print("PROJECTS")
    print("____________")
    A.execute("SELECT * from PROJECTS")
    P=A.fetchall()
    for i in P:
        print("PROJECT_ID:",i[0])
        print("PROJECT_NAME:",i[1])
        print("COUNTRY_OF_ORIGIN:",i[2])
        print("DATE_OF_INITIATION:",i[3])
        print("EXPECTED ARRIVAL:",i[4])
        print("COST_OF_PRODUCTION",i[5])
        print("COST_OF_TRANSPORTATION:",i[6])
        print("TOTAL COST:",i[7])
        print("________________________________________________________________________________")
    print("")
    print("CLIENTS")
    print("________________")
    A.execute("SELECT * from CLIENTS")
    P=A.fetchall()
    for i in P:
        print("CLIENT_ID:",i[0])
        print("USERNAME:",i[1])
        print("PASSWORD:",i[2])
        print("CLIENT_NAME:",i[3])
        print("CLIENT_CONTACT:",i[4])
        print("__________________________________________________________________________________")
    print("")
    print("SALES TRANSACTIONS")
    print("____________________")
    AA="SELECT * from SALES_TRANSACTIONS"
    A.execute(AA)
    we=A.fetchall()
    for i in we:
        print("PRODUCT_ID",i[0])
        print("QUANTITY",i[1])
        print("COST_PER_UNIT",i[2])
        print("COMPANY_NAME",i[3])
        print("TRANSACTION_ID",i[4])
        print("TOTAL_PAYMENT",i[5])
        print("USERNAME",i[6])
        print("______________________________________________________________________")
    print("")
    print("EMPLOYEE")
    print("________________")
    A.execute("SELECT * from EMPLOYEE")
    E=A.fetchall()
    for i in E:
        print("EMPLOYEE_ID:",i[0])
        print("EMPLOYEE_NAME:",i[1])
        print("DESIGNATION:",i[2])
        print("SALARY:",i[3])
        print("DATE_OF_JOIN:",i[4])
        print("MEDICAL_ALLOWENCE",i[5])
        print("ACCOMODATION_ALLOWENCE:",i[6])
        print("CONTACT_NO:",i[7])
        print("GENDER:",i[8])
        print("DOB:",i[9])
        print("_____________________________________________________________________")
    print("")
    print("CAREERS")
    print("____________")
    A.execute("SELECT * from CAREERS")
    CA=A.fetchall()
    for i in CA:
        print("DESIGNATION:",i[0])
        print("SALARY OFFERED:",i[1])
        print("REQUIRED QUALIFICATION:",i[2])
        print("REQUIRED YEARS OF SERVICES:",i[3])
        print("_____________________________________________________________________")
    print("")
    print("APPLICATIONS")
    A.execute("SELECT * from APPLICATIONS")
    C=A.fetchall()
    for i in C:
        print("DESIGNATION_APPLIED:",i[0])
        print("NAME:",i[1])
        print("QUALIFICATION:",i[2])
        print("YEARS OF SERVICES:",i[3])
        print("CONTACT INFO:",i[4])
        print("GENDER:",i[5])
        print("USER:",i[6])
        print("_____________________________________________________________________")
    print("")
    print("PERSONAL USERS")
    print("__________________")
    A.execute("SELECT * FROM PERSONAL_USER")
    U=A.fetchall()
    for i in U:
        print("USER:",i[0])
        print("PASSWORD:",i[1])
        print("SECURITY Q1",i[2])
        print("SECURITY Q2",i[3])
        print("SECURITY Q3",i[4])
        print("____________________________________________________________________")
    print("")
    print("EMPLOYEE USERS")
    print("____________________")
    A.execute("SELECT * FROM EMPLOYEE_USER")
    EU=A.fetchall()
    for i in EU:
        print("EMPLOYEE_ID:",i[0])
        print("USERNAME:",i[1])
        print("PASSWORD",i[2])
        print("ACCESS LEVEL",i[3])
        print("____________________________________________________________________")
    
    
def ADMIN(): #PASSWORD AND MENUS FOR ADMIN
    PASSWORD = getpass("ENTER THE ADMIN PASSWORD: ") 
    if PASSWORD=='TP2005-06':
        BOOT_UP()
        from time import sleep
        delay=20
        sleep(delay)
        from pygame import mixer
        mixer.init()
        mixer.music.load('NEW INTRO.mp3')
        mixer.music.play()
        while True:
            print("")
            print("0. DATA ANALYSIS")
            print("1. PROJECT PROGRESS")
            print("2. PRODUCTS CATALOGE")
            print("3. CLIENTS & DEALS")
            print("4. RECRUITMENT")
            print("5. WORK FORCE")
            print("6. ORDERS")
            print("7. USERS")
            print("8. EXCLUSIVE ACCESS")
            print("9. LOG OUT")
            print("")
            MC=int(input("WHAT WOULD LIKE TO DO FOR THE DAY? "))
            if MC==0:
                DATA()
            if MC==1:
                print('PROJECT PROGRESS')
                print("")
                print("1. NEW PROJECT FILE")
                print("2. DELETE PROJECTS")
                print("3. UPDDATE PROJECT SPECIFICS")
                MC1=int(input("WHAT WOULD YOU LIKE TO TAKE A LOOK AT? "))
                if MC1==1:
                    ADD_TO_RESEARCH()
                elif MC1==2:
                    DELETE_PROJECT()
                elif MC1==3:
                    UPDATE_PROJECT_INFO()
                else:
                    print("SIR, YOU HAVEN'T CHOSEN A VALID COMMAND")
            elif MC==2:
                print("PRODUCT CATALOGE")
                print("")
                print("1. NEW PRODUCT LAUNCH")
                print("2. TAKE DOWN UNDERPERFORMING PRODUCTS")
                print("3. UPDATE EXSISTING PRODUCT SPECIFICS")
                MC2=int(input("ANY CHANGES TO BE MAKE SIR? "))
                if MC2==1:
                    print("PRODUCT LAUNCHES")
                    print("")
                    ADD_TO_CATALOGE()
                elif MC2==2:
                    print("PRODUCT RETIREMENTS")
                    print("")
                    DELETE_CATALOGE()
                elif MC2==3:
                    print("UPDATE PRODUCT SPECIFICS")
                    print("")
                    UPDATE_PRODUCT_INFO()
                else:
                    print("TIRED SIR?, INVALID COMMAND ENTERED")
            elif MC==3:
                print("CLIENTS & DEALS")
                print("")
                print("1. UPDATE EXSISTING RELATIONS")
                print("2. DISOLVE CLIENT CONTRACTS")
                MC3=int(input("YOUR CHOICE SIR?"))
                if MC3==1:
                    print("RENEWALS/UPDATE TERMS")
                    print("")
                    UPDATE_CLIENT_DETAILS()
                elif MC3==2:
                    print("TERMINATE AGREEMENTS")
                    print("")
                    DELETE_CLIENTS_ADMIN()
                else:
                    print("WRITE TO BE UNDERSTOOD,SPEAK TO BE HEARD,READ TO GROW...INVALID CHOICE SIR")
            elif MC==4:
                print("RECRUITMENT")
                print("")
                print("1. CAREER SIGNUPS")
                print("2. RECRUITMENT PROCEDURE")
                print("")
                MC4=int(input("RECRUITING OR ISSUING A DEMAND GENIUSES ARE WE SIR?"))
                if MC4==1:
                    print("CAREER SIGNUP POSTS")
                    print("")
                    print("1. PUT UP OPENINGS")
                    print("2. UPDATE REQUIREMENTS")
                    print("3. DELETE OLD/EXPIRED POSTS")
                    MCH1=int(input("ENTER YOUR CHOICE SIR: "))
                    if MCH1==1:
                        ADD_TO_CAREERS()
                    elif MCH1==2:
                        UPDATE_CAREERS()
                    elif MCH1==3:
                        DELETE_OPENING()
                elif MC4==2:
                    print("RECRUITMENT PROCEDURES")
                    print("")
                    print("FOUND A GENIUS...HAVE YOU SIR?")
                    ADD_TO_EMPLOYEE()
            elif MC==5:
                print("WORK FORCE")
                print("")
                print("1. UPDATE EMPLOYEE DETAILS")
                print("2. DELETE EMPLOYEE DETAILS")
                MC5=int(input("WHAT DO YOU WANT TO DO SIR?"))
                if MC5==1:
                    UPDATE_EMPLOYEE_DETAILS()
                if MC5==2:
                    DELETE_EMPLOYEE()
            elif MC==6:
                print("ORDERS")
                print("")
                A.execute("SELECT * from SALES_TRANSACTIONS")
                print(A.fetchall())
                q=input("DELETE COMPLETED ORDERS?: (Y/N) ")
                if q.lower()=='n':
                    break
                else:
                    CANCEL_ORDERS()
                C1=input("BACK TO MAIN MENU? Y/N ")
                if C1.upper()=='N':
                    exit()
                else:
                    pass
            elif MC==7:
                print("USERS")
                print("1. VIEW")
                print("2. DELETE SPAM/BOTS")
                MC7=int(input("SIR, WHAT DO YOU WANT TO CHECK OUR USERS?"))
                if MC7==1:
                    A.execute("SELECT * FROM PERSONAL_USER")
                    U=A.fetchall()
                    for i in U:
                        print("USER:",i[0])
                        print("PASSWORDP:",i[1])
                        print("SECURITY Q1",i[2])
                        print("SECURITY Q2",i[3])
                        print("SECURITY Q3",i[4])
                        print("____________________________________________________________________")
                if MC7==2:
                    A.execute("SELECT * FROM PERSONAL_USER")
                    print(A.fetchall())
                    print("")
                    DELETE_USER()
            elif MC==8:
                SELECTED_ACCESS()
            elif MC==9:
                print("SUCCESSFULLY LOGGED OUT!")
                break
            else:
                print("INVALID COMMAND")
            
    from time import sleep
    if PASSWORD!="TP2005-06":
        print("HIGH SECURITY SEQUENCE INITIANTED...")
        delay=2
        sleep(delay)
        print("YOU ARE NOW LOCKED OUT OF THE ACCOUNT PLEASE CONTANCT THE IT DEPARTMENT @ PERFICIENT")
        exit()
        
def EMPLOYEE(): #EMPLOYEE MENUS
    from pygame import mixer
    mixer.init()
    mixer.music.load('EMP.mp3')
    mixer.music.play()
    u=input("ENTER YOUR USERNAME: ")
    p=getpass("ENTER YOUR PASSWORD: ")
    SQL321="SELECT PASSWORD FROM EMPLOYEE_USER WHERE USERNAME='{}'".format(u)
    A.execute(SQL321)
    p1=A.fetchall()
    P=list(p1[0])
    for i in P:
        if i==p:
            SQL322="SELECT ACCESS FROM EMPLOYEE_USER WHERE USERNAME='{}'".format(u)
            A.execute(SQL322)
            p12=A.fetchall()
            P123=str(p12[0][0])
            print(P123)
            A1="SALES_MANAGER"
            A2="PROJECT_DESIGNER"
            A3="PRODUCT_MANAGER"
            A4="HR"
            if P123==A1:
                SALES_MANAGER()
                break
            elif P123==A2:
                PROJECT_DESIGNER()
                break
            elif P123==A3:
                PRODUCT_MANAGER()
                break
            elif P123==A4:
                HR()
                break
            else:
                print("INVALID!")
                break
        if i!=p:
            CHANGEPASS=input("DO YOU WANT TO CHAGE YOUR PASSWORD? (Y/N) ")
            if CHANGEPASS.lower()=='y':
                NP=getpass("ENTER YOUR NEW PASSWORD: ")
                CP=getpass("CONFIRM YOUR NEW PASSWORD: ")
                if NP==CP:
                    SQL270="UPDATE PERSONAL_USER SET PASSWORD='{}' WHERE USERNAME='{}'".format(CP,u)
                    A.execute(SQL270)
                    con.commit()
                    print("")
                    print("SUCESSFULLY UPDATED")
                    print("")
            else:
                pass
    
def USER(): #USER MENU
    while True:
        mixer.init()
        mixer.music.load('BGM FOR USER.mp3')
        mixer.music.play()
        print("ACCOUNT TYPES")
        print("1. BUSINESS ACCOUNT")
        print("2. PERSONAL ACCOUNT")      
        USER_TYPE=int(input("ENTER YOUR ACCOUNT TYPE: "))
        if USER_TYPE==1:
            BUSINESS_USER()
        elif USER_TYPE==2:
            PERSONAL_USER()
        else:
            print("INVALID COMMAND!")
            break
            
def BUSINESS_USER(): #ALLOWS A BUSINESS USER TO ACCESS OR CREATE AN ACCOUNT (WITH SECURED PASSWORD AND SECURITY CODE LOGIN
    USER_NAME=input("ENTER YOUR USERNAME: ")
    SQL50="SELECT PASSWORD FROM CLIENTS WHERE USERNAME='{}'".format(USER_NAME)
    A.execute(SQL50)
    R=A.fetchall()
    if R!=[]:
        PASSWORD=getpass("ENTER YOUR PASSWORD: ")
        P=list(R)
        if PASSWORD==P[0][0]:
            SQL50="SELECT CLIENT_ID FROM CLIENTS WHERE USERNAME='{}'".format(USER_NAME)
            A.execute(SQL50)
            SC=A.fetchall()
            print("SECURITY CODE:",SC[0][0])
            print("WELCOME BACK TO PERFICIENT MR.",USER_NAME)
            print("WHAT WOULD YOU LIKE TO EXPLORE FOR THE DAY?")
            print("1. PLACE AN ORDER")
            print("2. EDIT EXSISTING ORDERS")
            print("3. EXIT")
            print("4. DELETE ACCOUNT")
            CHOICE_1=int(input("ENTER YOUR CHOICE "))
            if CHOICE_1==1:
                print("PLACE ORDERS WITH US NOW!")
                print("")
                ADD_TO_SALES()
            elif CHOICE_1==2:
                print("ALREADY ORDERED?")
                print("EDIT YOUR ORDER NOW!")
                print("1. UPDATE ORDERS")
                print("2. DELETE ORDERS")
                C=int(input("ENTER YOUR CHOICE: "))
                if C==1:
                    UPDATE_SALES()
                elif C==2:
                    CANCEL_ORDERS()
            elif CHOICE_1==3:
                print("THANK YOU!")
            elif CHOICE_1==4:
                DELETE_CLIENTS()
            else:
                print("OOPS! WRONG KEYS!!")
        elif PASSWORD!=P[0][0]:
            print("INCORRECT PASSWORD!")
            print("PLEASE ENTER THE SECURITY CODE PROVIDED DURING THE CREATION OF THE ACCOUNT TO VERIFY YOUR IDENTITY!!")
            SC=getpass("ENTER YOUR SECURITY CODE: ")
            SQL52="SELECT CLIENT_ID FROM CLIENTS WHERE USERNAME='{}'".format(USER_NAME)
            A.execute(SQL52)
            R1=A.fetchall()
            if R1[0][0]==SC:
                CHANGEPASS=input("DO YOU WANT TO CHAGE YOUR PASSWORD? (Y/N) ")
                if CHANGEPASS.lower()=='y':
                    NP=getpass("ENTER YOUR NEW PASSWORD: ")
                    CP=getpass("CONFIRM YOUR NEW PASSWORD: ")
                    if NP==CP:
                        SQL270="UPDATE CLIENTS SET PASSWORD='{}' WHERE USERNAME='{}'".format(CP,USER_NAME)
                        A.execute(SQL270)
                        con.commit()
                        print("")
                        print("SUCESSFULLY UPDATED")
                        print("")
                    if CHANGEPASS.lower()=='n':
                        pass
    
                SQL50="SELECT CLIENT_ID FROM CLIENTS WHERE USERNAME='{}'".format(USER_NAME)
                A.execute(SQL50)
                SC=A.fetchall()
                print("SECURITY CODE:",SC[0][0])
                print("WELCOME BACK TO PERFICIENT MR.",USER_NAME)
                print("WHAT WOULD YOU LIKE TO EXPLORE FOR THE DAY?")
                print("1. PLACE AN ORDER")
                print("2. EDIT EXSISTING ORDERS")
                print("3. EXIT")
                CHOICE_1=int(input("ENTER YOUR CHOICE "))
                if CHOICE_1==1:
                    print("PLACE ORDERS WITH US NOW!")
                    print("")
                    print("PRODUCTS ON SALE")
                    A.execute("SELECT * from CATALOGE")
                    print(A.fetchall())
                    ADD_TO_SALES()
                elif CHOICE_1==2:
                    print("ALREADY ORDERED?")
                    print("EDIT YOUR ORDER NOW!")
                    print("1. UPDATE ORDERS")
                    print("2. DELETE ORDERS")
                    C=int(input("ENTER YOUR CHOICE: "))
                    if C==1:
                        UPDATE_SALES()
                    elif C==2:
                        CANCEL_ORDERS()
                elif CHOICE_1==3:
                    print("THANK YOU!")
                else:
                    print("OOPS! WRONG KEYS!!")
    else:
        print("CREATE YOUR USER ACCOUNT TODAY!")
        C1=input("SIGN UP? Y/N ")
        if C1.upper()=='N':
            exit()
        else:
            ADD_TO_CLIENT()
            
def PERSONAL_USER(): #ALLOWS A BUSINESS USER TO ACCESS OR CREATE AN ACCOUNT (SECURED WITH A PASSWORD AND 3 SECURITY QUESTIONS)
    USER_NAME1=input("ENTER YOUR USERNAME: ")
    SQL51="SELECT PASSWORD FROM PERSONAL_USER WHERE USERNAME='{}'".format(USER_NAME1)
    A.execute(SQL51)
    R=A.fetchall()
    if R!=[]:
        PASSWORD=getpass("ENTER YOUR PASSWORD: ")
        P=list(R)
        if PASSWORD==P[0][0]:
            while True:
                print("MAIN MENU")
                print("")
                print("1. VIEW CAREER OPPORTUNITIES")
                print("2. FILL UP YOUR RESUME")
                print("3. UPDATE EXSISTING APPLICATIONS")
                print("4. AWARDS AND ACCOLADES")
                print("5. TRACK RECORD")
                print("6. CONTACT US")
                print("7. DELETE ACCOUNT")
                print("8. LOG OUT")
                CHOICE_2=int(input("ENTER YOUR CHOICE: "))
                if CHOICE_2==1:
                    A.execute("SELECT * from CAREERS")
                    print(A.fetchall())
                    print("")
                    print("DON'T POSTPONE YOUR DREAMS!")
                    print("SUBMIT YOUR CV TODAY! ")
                    c1=input("GO TO CAREER APPLICATIONS? Y/N")
                    if c1.upper()=='Y':
                        ADD_TO_APPLICATIONS()
                    else:
                        pass
                if CHOICE_2==2:
                    ADD_TO_APPLICATIONS()
                if CHOICE_2==3:
                    UPDATE_APPLICATIONS()
                if CHOICE_2==4:
                    print("AWARDS AND ACCOLADES:")
                    print("""WE HERE AT PERFICIENT BELIVE IN RECOGNISING THE EFFORTS OF THE MASSES, WHICH IS WHY WE HAVE PATNERED WITH NASA TO BRING TO YOU THE HIGHEST NUMBER OF EMPLOYEE ACCOLADES OFFICIALLY RECOGNISED BY SPACE AGENCIES AROUND THE WORLD
                            
                            Distinguished Service Medal
                            Distinguished Public Service Medal
                            Outstanding Leadership Medal
                            Outstanding Public Leadership Medal
                            Exceptional Service Medal
                            Exceptional Public Service Medal
                            Exceptional Bravery Medal
                            Exceptional Engineering Achievement Medal
                            Exceptional Scientific Achievement Medal
                            Exceptional Technology Achievement Medal
                            Equal Employment Opportunity Medal
                            Exceptional Administrative Achievement Medal
                            Exceptional Achievement Medal
                            Exceptional Public Achievement Medal
                            Early Career Achievement Medal
                            Early Career Public Achievement Medal
                            Silver Achievement Medal
                            Group Achievement Award
                            Space Flight Medal
                            
                            SO WHY WAIT? JOIN OUR FAMILY TODAY!
                            ARE YOU UP TO THE CHALLENGE OF ACHIEVING AN EARLY CAREER MEDAL?
                            START YOUR APPLICATION PROCCESS TODAY!""")
                    print("")
                    c1=input("GO TO CAREER APPLICATIONS? Y/N")
                    if c1.upper()=='Y':
                        ADD_TO_APPLICATIONS()
                    else:
                        pass
                if CHOICE_2==5:
                    import random
                    SC=random.randint(100,999)
                    P=random.randint(10,100)
                    OC=random.randint(10,100)
                    print("OUR IMPRESSIVE TRACK RECORDS!")
                    print(SC,"MILLION SATISFIED CUSTOMERS!")
                    print(P,"THOUSAND SPECIAL PARTNERS INCLUDING THE LIKES OF NASA,ISRO AND SPACEX!")
                    print(OC,"BILLION ORDERS COMPLETED SUCCESSFULLY!")
                    print("")
                    print("DO YOU WANT TO BE PART OF THE FUTURE THAT LIES AHEAD?")
                    print("START YOUR APPLICATION PROCESS NOW!")
                    print("")
                    c1=input("GO TO CAREER APPLICATIONS? Y/N")
                    if c1.upper()=='Y':
                        ADD_TO_APPLICATIONS()
                    else:
                        pass
                if CHOICE_2==6:
                    print("QUIRES? QUESTIONS? APPLICATION STATUS?")
                    print("FEEL FREE TO CONTACT US ON:")
                    print("EMAIL: QUIRES@PERFICIENT.COM")
                    print("CHAT WITH US ON 232-243-4480")
                    print("AN OFFICIAL AWAITS YOUR CALL!")
                    
                if CHOICE_2==7:
                    DELETE_USER()
                if CHOICE_2==8:
                    print("THANK YOU FOR CHOOSING PERFICIENT!")
                    break
            
        if PASSWORD!=P[0][0]:
            print("INCORRECT PASSWORD!")
            print("PLEASE ANSWER THESE SECURITY QUESTIONS TO SUCCESSFULLY VERIFY YOUR IDENTITY!")
            print("")
            SQL51="SELECT SQ1,SQ2,SQ3 FROM PERSONAL_USER WHERE USERNAME='{}'".format(USER_NAME1)
            A.execute(SQL51)
            R11=A.fetchall()
            A1=input("SECURITY_QUESTION_1: FAVOURITE FOOD: ")
            if R11[0][0]==A1:
                A2=input("SECURITY_QUESTION_2: WHERE DID YOU GO WHEN YOU FLEW FOR THE FIRST TIME: ")
                if R11[0][1]==A2:
                    A3=input("SECURITY_QUESTION_3: DREAM JOB: ")
                    if R11[0][2]==A3:
                        CHANGEPASS=input("DO YOU WANT TO CHAGE YOUR PASSWORD? (Y/N) ")
                        if CHANGEPASS.lower()=='y':
                            NP=getpass("ENTER YOUR NEW PASSWORD: ")
                            CP=getpass("CONFIRM YOUR NEW PASSWORD: ")
                            if NP==CP:
                                SQL270="UPDATE PERSONAL_USER SET PASSWORD='{}' WHERE USERNAME='{}'".format(CP,USER_NAME1)
                                A.execute(SQL270)
                                con.commit()
                                print("")
                                print("SUCESSFULLY UPDATED")
                                print("")
                            else:
                                print("UPDATE UNSUCCESSFULL!")
                        else:
                            pass
    
                        while True:
                            print("MAIN MENU")
                            print("")
                            print("1. VIEW CAREER OPPORTUNITIES")
                            print("2. FILL UP YOUR RESUME")
                            print("3. UPDATE EXSISTING APPLICATIONS")
                            print("4. AWARDS AND ACCOLADES")
                            print("5. TRACK RECORD")
                            print("6. CONTACT US")
                            print("7. DELETE ACCOUNT")
                            print("8. LOG OUT")
                            CHOICE_2=int(input("ENTER YOUR CHOICE: "))
                            if CHOICE_2==1:
                                A.execute("SELECT * from CAREERS")
                                print(A.fetchall())
                                print("")
                                print("DON'T POSTPONE YOUR DREAMS!")
                                print("SUBMIT YOUR CV TODAY! ")
                                c1=input("GO TO CAREER APPLICATIONS? Y/N")
                                if c1.upper()=='Y':
                                    ADD_TO_APPLICATIONS()
                                else:
                                    pass
                            if CHOICE_2==2:
                                ADD_TO_APPLICATIONS()
                            if CHOICE_2==3:
                                UPDATE_APPLICATIONS()
                            if CHOICE_2==4:
                                print("AWARDS AND ACCOLADES:")
                                print("""WE HERE AT PERFICIENT BELIVE IN RECOGNISING THE EFFORTS OF THE MASSES, WHICH IS WHY WE HAVE PATNERED WITH NASA TO BRING TO YOU THE HIGHEST NUMBER OF EMPLOYEE ACCOLADES OFFICIALLY RECOGNISED BY SPACE AGENCIES AROUND THE WORLD
                                        
                                        Distinguished Service Medal
                                        Distinguished Public Service Medal
                                        Outstanding Leadership Medal
                                        Outstanding Public Leadership Medal
                                        Exceptional Service Medal
                                        Exceptional Public Service Medal
                                        Exceptional Bravery Medal
                                        Exceptional Engineering Achievement Medal
                                        Exceptional Scientific Achievement Medal
                                        Exceptional Technology Achievement Medal
                                        Equal Employment Opportunity Medal
                                        Exceptional Administrative Achievement Medal
                                        Exceptional Achievement Medal
                                        Exceptional Public Achievement Medal
                                        Early Career Achievement Medal
                                        Early Career Public Achievement Medal
                                        Silver Achievement Medal
                                        Group Achievement Award
                                        Space Flight Medal
                                        
                                        SO WHY WAIT? JOIN OUR FAMILY TODAY!
                                        ARE YOU UP TO THE CHALLENGE OF ACHIEVING AN EARLY CAREER MEDAL?
                                        START YOUR APPLICATION PROCCESS TODAY!""")
                                print("")
                                c1=input("GO TO CAREER APPLICATIONS? Y/N")
                                if c1.upper()=='Y':
                                    ADD_TO_APPLICATIONS()
                                else:
                                    pass
                            if CHOICE_2==5:
                                import random
                                SC=random.randint(100,999)
                                P=random.randint(10,100)
                                OC=random.randint(10,100)
                                print("OUR IMPRESSIVE TRACK RECORDS!")
                                print(SC,"MILLION SATISFIED CUSTOMERS!")
                                print(P,"THOUSAND SPECIAL PARTNERS INCLUDING THE LIKES OF NASA,ISRO AND SPACEX!")
                                print(OC,"BILLION ORDERS COMPLETED SUCCESSFULLY!")
                                print("")
                                print("DO YOU WANT TO BE PART OF THE FUTURE THAT LIES AHEAD?")
                                print("START YOUR APPLICATION PROCESS NOW!")
                                print("")
                                c1=input("GO TO CAREER APPLICATIONS? Y/N")
                                if c1.upper()=='Y':
                                    ADD_TO_APPLICATIONS()
                                else:
                                    pass
                            if CHOICE_2==6:
                                print("QUIRES? QUESTIONS? APPLICATION STATUS?")
                                print("FEEL FREE TO CONTACT US ON:")
                                print("EMAIL: QUIRES@PERFICIENT.COM")
                                print("CHAT WITH US ON 232-243-4480")
                                print("AN OFFICIAL AWAITS YOUR CALL!")
                                
                            if CHOICE_2==7:
                                DELETE_USER()
                            if CHOICE_2==8:
                                print("THANK YOU FOR CHOOSING PERFICIENT!")
                                break
                        
                    else:
                        print("YOU HAVE BEEN LOCK OUT OF YOUR ACCOUNT, PLEASE CONTACT US FOR FURTHER VERIFICATION")
                        exit()
                else:
                    print("YOU HAVE BEEN LOCK OUT OF YOUR ACCOUNT, PLEASE CONTACT US FOR FURTHER VERIFICATION")
                    exit()
            else:
                print("YOU HAVE BEEN LOCK OUT OF YOUR ACCOUNT, PLEASE CONTACT US FOR FURTHER VERIFICATION")
                exit()
                    
    else:
        print("CREATE A USERNAME TODAY!")
        C1=input("SIGN UP? Y/N ")
        if C1.upper()=='N':
            exit()
        while True:
            NU=input("ENTER NEW USERNAME: ")
            SQL78="SELECT USERNAME FROM PERSONAL_USER"
            A.execute(SQL78)
            W1=A.fetchall()
            w=list(W1[0])
            for i in w:
                if i!=NU:
                    NP=getpass("ENTER NEW PASSWORD: ")
                    CNP=getpass("CONFIRM YOUR PASSWORD: ")
                    SQ1=input("SECURITY_QUESTION_1: FAVOURITE FOOD: ")
                    SQ2=input("SECURITY_QUESTION_1: WHERE DID YOU GO WHEN YOU FLEW FOR THE FIRST TIME: ")
                    SQ3=input("SECURITY_QUESTION_1: DREAM JOB: ")
                    if NP==CNP:
                        SQL77="INSERT INTO PERSONAL_USER VALUES('{}','{}','{}','{}','{}')".format(NU,NP,SQ1,SQ2,SQ3)
                        A.execute(SQL77)
                        con.commit()
                        print("USER CREATED! REFREASH THE PAGE TO LOG IN!")
                        exit()
                    else:
                        print("PLEASE RE-CHECK YOUR PASSWORD!")
                else:
                    print("USERNAME ALREADY EXSISTS!")

def HR(): #HR DEPARTMENT MENU
    while True:
        print("“Train people well enough so they can leave. Treat them well enough so they don’t want to.” – Sir Richard Branson ")
        print("")
        print("RECRUITMENT")
        print("MAIN MENU")
        print("1. CAREER SIGNUPS")
        print("2. RECRUITMENT PROCEDURE")
        MC4=int(input("WHAT WOULD YOU LIKE TO DO TODAY? "))
        if MC4==1:
            print("CAREER SIGNUP POSTS")
            print("")
            print("1. PUT UP OPENINGS")
            print("2. UPDATE REQUIREMENTS")
            print("3. DELETE OLD/EXPIRED POSTS")
            MCH1=int(input("ENTER YOUR CHOICE SIR: "))
            if MCH1==1:
                ADD_TO_CAREERS()
            elif MCH1==2:
                UPDATE_CAREERS()
            elif MCH1==3:
                DELETE_OPENING()
        elif MC4==2:
            print("RECRUITMENT PROCEDURES")
            print("")
            print("")
            ADD_TO_EMPLOYEE()
        else:
            pass
        C1=input("BACK TO MAIN MENU? Y/N ")
        if C1.upper()=='N':
            exit()
        else:
            pass

def PRODUCT_MANAGER(): #PRODUCT MENU
    while True:
        print("PRODUCT CATALOGE")
        print("")
        print("MAIN MENU")
        print("1. NEW PRODUCT LAUNCH")
        print("2. TAKE DOWN UNDERPERFORMING PRODUCTS")
        print("3. UPDATE EXSISTING PRODUCT SPECIFICS")
        print("4. DELETE COMPLETE ORDERS")
        MC2=int(input("ANY CHANGES TO BE MADE? "))
        if MC2==1:
            print("PRODUCT LAUNCHES")
            print("")
            ADD_TO_CATALOGE()
        elif MC2==2:
            print("PRODUCT RETIREMENTS")
            print("")
            DELETE_CATALOGE()
        elif MC2==3:
            print("UPDATE PRODUCT SPECIFICS")
            print("")
            UPDATE_PRODUCT_INFO()
        elif MC2==4:
            print("DELETE COMPLETE ORDERS")
            print("")
            CANCEL_ORDERS()
        else:
            print("TIRED SIR?, INVALID COMMAND ENTERED")
    
def PROJECT_DESIGNER(): #PROJECT MENU
    while True:
        print('PROJECT PROGRESS')
        print("")
        print("1. NEW PROJECT FILE")
        print("2. DELETE PROJECTS")
        print("3. UPDDATE PROJECT SPECIFICS")
        MC1=int(input("WHAT WOULD YOU LIKE TO TAKE A LOOK AT? "))
        if MC1==1:
            ADD_TO_RESEARCH()
        elif MC1==2:
            DELETE_PROJECT()
        elif MC1==3:
            UPDATE_PROJECT_INFO()
        else:
            print("INVALID COMMAND")
        C1=input("BACK TO MAIN MENU? Y/N ")
        if C1.upper()=='N':
            exit()
        else:
            pass

def DELETE_USER(): #ALLOWS USERS TO DELETE THEIR ACCOUNTS
    P=getpass("ENTER YOUR PASSWORD: ")
    USERNAME12=input("PLEASE CONFIRM YOUR USERNAME:")
    SQL51="SELECT SQ1,SQ2,SQ3 FROM PERSONAL_USER WHERE PASSWORD='{}' AND USERNAME='{}'".format(P,USERNAME12)
    A.execute(SQL51)
    R11=A.fetchall()
    A1=input("SECURITY_QUESTION_1: FAVOURITE FOOD: ")
    if R11[0][0]==A1:
        A2=input("SECURITY_QUESTION_2: WHERE DID YOU GO WHEN YOU FLEW FOR THE FIRST TIME: ")
        if R11[0][1]==A2:
            A3=input("SECURITY_QUESTION_3: DREAM JOB: ")
            if R11[0][2]==A3:
                R=input("ARE YOU SURE? ")
                if R.upper()=='Y':
                    SQL75="DELETE FROM PERSONAL_USER WHERE USERNAME='{}'".format(USERNAME12)
                    A.execute(SQL75)
                    con.commit()
                    print("SUCCESSFULLY DELETED!")
                    exit()
                else:
                    pass
    
def SELECTED_ACCESS(): #EMPLOYEE DESIGNATED AREAS
    while True:
        NAME=input("ENTER EMPLOYEE'S NAME: ")
        D=input("ENTER ACCESS LEVEL: ")
        if D.upper() in ['HR','PROJECT DESIGNER','PRODUCT MANAGER']:
            NU1=input("ENTER NEW USERNAME: ")
            SQL781="SELECT USERNAME FROM EMPLOYEE_USER"
            A.execute(SQL781)
            W11=A.fetchall()
            if NU1 not in W11:
                SQL7812="SELECT * FROM EMPLOYEE WHERE EMPLOYEE_NAME='{}'".format(NAME)
                A.execute(SQL7812)
                W112=A.fetchall()
                print(W112)
                if W112!=[]:
                    NO=str(W112[0][0])
                    NP=getpass("ENTER NEW PASSWORD: ")
                    CNP=getpass("CONFIRM YOUR PASSWORD: ")
                    print(NO)
                    if NP==CNP:
                        SQL772="INSERT INTO EMPLOYEE_USER VALUES('{}','{}','{}','{}')".format(NO,NU1,NP,D)
                        A.execute(SQL772)
                        con.commit()
                        print("USER CREATED! REFREASH THE PAGE TO LOG IN!")
                        c=input("DO YOU WANT TO CONTINUE?(Y/N): ")
                        if c.lower()=="n":
                            break
                        else:
                            pass
                    else:
                        print("PLEASE RE-CHECK YOUR PASSWORD!")
                else:
                    print("NO RECORDS AVAILABLE!")
            else:
                print("USERNAME ALREADY EXSISTS!")
        else:
            print("ACCESS LEVEL INVALID")

def ADD_TO_CATALOGE(): #ALLOWS THE ADMIN TO ADD ENTRIES TO THE CATALOGE TABLE
    while True:
        print("PRODUCTS ON SALE: ")
        A.execute("SELECT * from CATALOGE")
        Q=A.fetchall()
        for i in Q:
            print("PRODUCT_ID:",i[0])
            print("PRICE:",i[1])
            print("PRODUCT NAME:",i[2])
            print("________________________________________________________________________________")
        import random
        PRODUCT_ID=random.randint(1,10000)
        PRODUCT_NAME=input("ENTER PRODUCT NAME: ")
        PRICE=input("ENTER THE PRICE OF PRODUCT: ")
        SQL="INSERT INTO CATALOGE VALUES('{}','{}','{}')".format(PRODUCT_ID,PRICE,PRODUCT_NAME)
        A.execute(SQL)
        con.commit()
        print("")
        print("SUCESSFULLY UPDATED")
        A.execute("SELECT * from CATALOGE")
        PR=A.fetchall()
        for i in PR:
            print("PRODUCT_ID:",i[0])
            print("PRICE:",i[1])
            print("PRODUCT NAME:",i[2])
            print("_________________________________________________________________________________")
        CONTINUE=input("DO YOU WANT TO CONTINUE? (Y/N) ")
        if CONTINUE.upper()=='N':
            break
        C1=input("BACK TO MAIN MENU? Y/N ")
        if C1.upper()=='N':
            exit()
        else:
            continue

def ADD_TO_RESEARCH(): #ALLOWS THE ADMIN TO ADD ENTRIES TO THE PROJECTS TABLE
    while True:
        import random
        PROJECT_ID=random.randint(1,10000)
        PROJECT_NAME=input("ENTER THE PROJECT NAME: ")
        COUNTRY_OF_ORIGIN=input("ENTER THE COUNTRY OF MAKE: ")
        DATE_OF_INITIATION=input("ENTER THE INTIATION DATE: ")
        EXPECTED_ARRIVAL=input("ENTER LAUNCH DATE: ")
        COST_OF_PRODUCTION=input("ENTER THE COST OF PRODUCTION: ")
        COST_OF_TRANSPORT=input("ENTER THE TRANSPORTATION COST: ")
        TOTAL_COST=float(COST_OF_TRANSPORT)+float(COST_OF_PRODUCTION)
        SQL1="INSERT INTO PROJECTS VALUES('{}','{}','{}','{}','{}','{}','{}','{}')".format(PROJECT_ID,PROJECT_NAME,COUNTRY_OF_ORIGIN,DATE_OF_INITIATION,EXPECTED_ARRIVAL,COST_OF_PRODUCTION,COST_OF_TRANSPORT,TOTAL_COST)
        A.execute(SQL1)
        con.commit()
        print("SUCESSFULLY ADDED")
        print("")
        A.execute("SELECT * from PROJECTS")
        P=A.fetchall()
        for i in P:
            print("PROJECT_ID:",i[0])
            print("PROJECT_NAME:",i[1])
            print("COUNTRY_OF_ORIGIN:",i[2])
            print("DATE_OF_INITIATION:",i[3])
            print("EXPECTED ARRIVAL:",i[4])
            print("COST_OF_PRODUCTION",i[5])
            print("COST_OF_TRANSPORTATION:",i[6])
            print("TOTAL COST:",i[7])
            print("________________________________________________________________________________")
        CONTINUE=input("DO YOU WANT TO CONTINUE? Y/N ")
        if CONTINUE.upper()=='N':
            break
        C1=input("BACK TO MAIN MENU? Y/N ")
        if C1.upper()=='N':
            exit()
        else:
            continue
        
def ADD_TO_CLIENT(): #ALLOWS THE USER TO ADD ENTRIES TO THE CLIENTS TABLE
    NEW_USERNAME=input("ENTER NEW USERNAME: ")
    SQL789="SELECT USERNAME FROM CLIENTS"
    A.execute(SQL789)
    W1=A.fetchall()
    if NEW_USERNAME not in W1:
        PASSWORD=getpass("ENTER YOUR PASSWORD: ")
        CP=getpass("CONFIRM YOUR PASSWORD: ")
        import random
        CLIENT_ID=random.randint(1,10000)
        CLIENT_NAME=input("ENTER THE CLIENT NAME: ")
        CLIENT_CONTACT=input("ENTER CLIENT CONTACT (EMAIL/PH NUMBER): ")
        if PASSWORD==CP:
            SQL2="INSERT INTO CLIENTS VALUES('{}','{}','{}','{}','{}')".format(CLIENT_ID,NEW_USERNAME,PASSWORD,CLIENT_NAME,CLIENT_CONTACT)
            A.execute(SQL2)
            con.commit()
            print("")
            print("SUCESSFULLY ADDED")
            print("")
            C1=input("BACK TO MAIN MENU? Y/N ")
            if C1.upper()=='N':
                exit()
            else:
                pass
        else:
            print("RECHECK YOUR PASSWORD!")
    else:
        print("USER ALREADY EXSISTS!")
        
def ADD_TO_SALES(): #ALLOWS THE USER TO ADD ENTRIES TO THE SALES_TRANSACTIONS TABLE
    print("PRODUCTS ON SALE: ")
    A.execute("SELECT * from CATALOGE")
    PRODUCTS=A.fetchall()
    for i in PRODUCTS:
        print("PRODUCT_ID:",i[0])
        print("PRICE:",i[1])
        print("PRODUCT NAME:",i[2])
        print("________________________________________________________________________________")
    C_UN=input("CONFIRM YOUR USERNAME: ")
    A.execute("SELECT USERNAME FROM CLIENTS")
    W=A.fetchall()
    SS="SELECT CLIENT_NAME FROM CLIENTS WHERE USERNAME='{}'".format(C_UN)
    A.execute(SS)
    W1=A.fetchall()
    W11=list(W1)
    print(W11)
    if C_UN in W[0]:
        print("PLEASURE DOING BUSINESS WITH YOU AGAIN, MR.",C_UN)
        if PRODUCTS!=[]:
            PRODUCT_ID=input("ENTER PRODUCT CODE: ")
            BB="SELECT PRODUCT_ID from CATALOGE WHERE PRODUCT_ID='{}'".format(PRODUCT_ID)
            A.execute(BB)
            IDS=A.fetchall()
            if IDS!=[]:
                SQL37="SELECT PRICE from CATALOGE WHERE PRODUCT_ID='{}'".format(PRODUCT_ID)
                A.execute(SQL37)
                P=A.fetchall()
                PL=list(P)
                QUANTITY=int(input("ENTER THE QUANTITY: "))
                COMPANY_NAME=W11[0][0]
                COST_PER_UNIT=PL[0][0]
                TOTAL_PAYMENT=int(COST_PER_UNIT)*int(QUANTITY)
                import random
                TRANSACTION_ID=random.randint(1,10000)
                SQL3="INSERT INTO SALES_TRANSACTIONS VALUES('{}','{}','{}','{}','{}','{}','{}')".format(PRODUCT_ID,QUANTITY,COST_PER_UNIT,COMPANY_NAME,TRANSACTION_ID,
                                                                                 TOTAL_PAYMENT,C_UN)
                A.execute(SQL3)
                con.commit()
                print("")
                print("SUCESSFULLY ADDED")
                AA="SELECT * from SALES_TRANSACTIONS WHERE COMPANY_NAME='{}'".format(COMPANY_NAME)
                A.execute(AA)
                we=A.fetchall()
                for i in we:
                    print("PRODUCT_ID",i[0])
                    print("QUANTITY",i[1])
                    print("COST_PER_UNIT",i[2])
                    print("COMPANY_NAME",i[3])
                    print("TRANSACTION_ID",i[4])
                    print("TOTAL_PAYMENT",i[5])
                    print("USERNAME",i[6])
                    print("______________________________________________________________________")
                C1=input("BACK TO MAIN MENU? Y/N ")
                if C1.upper()=='N':
                    exit()
                else:
                    pass
            else:
                print("INVALID PRODUCT ID")
    else:
        print("INVALID USERNAME")
    
                    
def ADD_TO_EMPLOYEE(): #ALLOWS THE ADMIN TO ADD ENTRIES TO THE EMPLOYEE TABLE
    while True:
        import random
        EMPLOYEE_ID=random.randint(1,10000)
        EMPLOYEE_NAME=input("ENTER THE EMPLOYEE NAME: ")
        D1="SELECT * FROM APPLICATIONS WHERE NAME='{}'".format(EMPLOYEE_NAME)
        A.execute(D1)
        DO1=A.fetchall()
        if DO1!=[]:
            DESIGNATION=DO1[0][0]
            GENDER=DO1[0][5]
            DOB=input("ENTER THE DOB OF EMPLOYEE: ")
            D2="SELECT SALARY FROM CAREERS WHERE DESIGNATION='{}'".format(DESIGNATION)
            A.execute(D2)
            DO2=A.fetchall()
            SALARY=DO2[0][0]
            DATE_OF_JOIN=input("ENTER THE DATE OF JOIN: ")
            MEDICAL_ALLOWENCE=float(SALARY)*0.2
            ACCOMODATION_ALLOWENCE=float(SALARY)*0.1
            CONTACT_NO=DO1[0][4]
            SQL4="INSERT INTO EMPLOYEE VALUES('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(EMPLOYEE_ID,EMPLOYEE_NAME,DESIGNATION,SALARY,DATE_OF_JOIN,
                                                                                                   MEDICAL_ALLOWENCE,ACCOMODATION_ALLOWENCE,CONTACT_NO,GENDER,DOB)
            A.execute(SQL4)
            con.commit()
            W1="DELETE FROM APPLICATIONS WHERE NAME='{}' AND DESIGNATION_APPLIED='{}'".format(EMPLOYEE_NAME,DESIGNATION)
            A.execute(W1)
            con.commit()
            print("")
            print("SUCESSFULLY ADDED")
            A.execute("SELECT * from EMPLOYEE")
            E=A.fetchall()
            for i in E:
                print("EMPLOYEE_ID:",i[0])
                print("EMPLOYEE_NAME:",i[1])
                print("DESIGNATION:",i[2])
                print("SALARY:",i[3])
                print("DATE_OF_JOIN:",i[4])
                print("MEDICAL_ALLOWENCE",i[5])
                print("ACCOMODATION_ALLOWENCE:",i[6])
                print("CONTACT_NO:",i[7])
                print("GENDER:",i[8])
                print("DOB:",i[9])
                print("_____________________________________________________________________")
            CONTINUE=input("DO YOU WANT TO CONTINUE? Y/N ")
            if CONTINUE.upper()!='Y':
                break
            C1=input("BACK TO MAIN MENU? Y/N ")
            if C1.upper()=='N':
                exit()
            else:
                continue
        else:
            print("NO APPLICATIONS AVAILABLE")
            
def ADD_TO_CAREERS(): #ALLOWS THE ADMIN TO ADD ENTRIES TO THE CAREERS TABLE
    while True:
        DESIGNATION=input("ENTER DESIGNATION: ")
        SALARY_NEW_EMP=input("ENTER THE SALARY OFFERED: ")
        REQ_QUAL=input("ENTER REQUIRED QUALIFICATION: ")
        REQ_YOE=input("ENTER THE REQUIRED YEARS OF SERVICE: ")
        SQL25="INSERT INTO CAREERS VALUES('{}','{}','{}','{}')".format(DESIGNATION,SALARY_NEW_EMP,REQ_QUAL,REQ_YOE)
        A.execute(SQL25)
        con.commit()
        print("")
        print("SUCESSFULLY ADDED")
        A.execute("SELECT * from CAREERS")
        CA=A.fetchall()
        for i in CA:
            print("DESIGNATION:",i[0])
            print("SALARY OFFERED:",i[1])
            print("REQUIRED QUALIFICATION:",i[2])
            print("REQUIRED YEARS OF SERVICES:",i[3])
            print("_____________________________________________________________________")
        CONTINUE=input("DO YOU WANT TO CONTINUE? Y/N ")
        print("")
        if CONTINUE.upper()=='N':
            break
        C1=input("BACK TO MAIN MENU? Y/N ")
        if C1.upper()=='N':
            exit()
        else:
            continue
            
def ADD_TO_APPLICATIONS(): #ALLOWS THE ADMIN TO ADD ENTRIES TO THE APPLICATIONS TABLE
    USER=input("CONFIRM YOUR USERNAME: ")
    A.execute("SELECT * from CAREERS")
    OPENINGS=A.fetchall()
    for i in OPENINGS:
        print("DESIGNATION:",i[0])
        print("SALARY OFFERED:",i[1])
        print("REQUIRED QUALIFICATION:",i[2])
        print("REQUIRED YEARS OF SERVICES:",i[3])
        print("_____________________________________________________________________")
    print("")
    A.execute("SELECT DESIGNATION from CAREERS")
    DES_AV=A.fetchall()
    if OPENINGS!=[]:
        print(DES_AV)
        print("")
        DESIGNATION_APP=input("ENTER DESIGNATION TO BE APPLIED FOR: ")
        SQL34="SELECT REQUIRED_YEARS_OF_EXPERIANCE,REQUIRED_QUALIFICATION from CAREERS WHERE DESIGNATION='{}'".format(DESIGNATION_APP)
        A.execute(SQL34)
        RYOE1=A.fetchall()
        print((RYOE1))
        print("")
        if RYOE1!=[]:
            REG_NAME=input("ENTER YOUR NAME: ")
            SQL480="SELECT * from APPLICATIONS WHERE NAME='{}'".format(REG_NAME)
            A.execute(SQL480)
            APPLS1=A.fetchall()
            if APPLS1==[]:
                REG=input("ENTER THEIR GENDER: ")
                CINFO=input("ENTER YOUR CONTACT INFO: ")
                QUAL=input("ENTER YOUR QUALIFICATION: ")
                YOE=input("ENTER YOUR YEARS OF EXPERIANCE: ")
                G=str(RYOE1[0][1])
                N=str(RYOE1[0][0])
                if QUAL==G and YOE>=N:
                    SQL30="INSERT INTO APPLICATIONS VALUES('{}','{}','{}','{}','{}','{}','{}')".format(DESIGNATION_APP,REG_NAME,QUAL,YOE,CINFO,REG,USER)
                    A.execute(SQL30)
                    con.commit()
                    print("SUCESSFULLY ADDED")
                    print("")
                    SQL40="SELECT * from APPLICATIONS WHERE NAME='{}'".format(REG_NAME)
                    A.execute(SQL40)
                    APPLS=A.fetchall()
                    print((APPLS))
                    C1=input("BACK TO MAIN MENU? Y/N ")
                    if C1.upper()=='N':
                        exit()
                    else:
                        pass
                else:
                    print("OPPS! YOU DO NOT MEET THE REQUIREMENTS")
            else:
                print("OTHER APPLICATIONS IN PROGRESS, PLEASE WAIT FOR A RESPONSE FROM OUR HR TEAM")
                SQL403="SELECT * from APPLICATIONS WHERE NAME='{}'".format(REG_NAME)
                A.execute(SQL403)
                APPLS3=A.fetchall()
                print((APPLS3))
        else:
            print("INVALID DESIGNATION ENTERED! PLEASE REFRESH YOUR PAGE TO SUBMIT A NEW FORM")
    else:
        print("OOPS! IT SEEMS NO OPENINGS ARE AVAILABLE AT THE MOMENT!")

def DELETE_PROJECT(): #ALLOWS THE ADMIN TO DELETE ENTRIES TO THE PROJECTS TABLE
    print("PROJECTS: ")
    A.execute("SELECT * from PROJECTS")
    PI=A.fetchall()
    for i in PI:
        print("PROJECT_ID:",i[0])
        print("PROJECT_NAME:",i[1])
        print("COUNTRY_OF_ORIGIN:",i[2])
        print("DATE_OF_INITIATION:",i[3])
        print("EXPECTED ARRIVAL:",i[4])
        print("COST_OF_PRODUCTION",i[5])
        print("COST_OF_TRANSPORTATION:",i[6])
        print("TOTAL COST:",i[7])
        print("________________________________________________________________________________")
    if PI!=[]:
        D=getpass("THE ID NUMBER OF PROJECT TO BE DELETED: ")
        SQL500="SELECT PROJECT_ID FROM PROJECTS WHERE PROJECT_ID=('{}')".format(D)
        A.execute(SQL500)
        C=A.fetchall()
        print("")
        if D in C[0][0]:
            S=input("ARE YOU SURE? (Y/N)")
            if S.upper()=='Y':
                SQL5="DELETE FROM PROJECTS WHERE PROJECT_ID=('{}')".format(D)
                A.execute(SQL5)
                con.commit()
                print("SUCESSFULLY DELETED")
                print("")
                A.execute("SELECT * from PROJECTS")
                P=A.fetchall()
                for i in P:
                    print("PROJECT_ID:",i[0])
                    print("PROJECT_NAME:",i[1])
                    print("COUNTRY_OF_ORIGIN:",i[2])
                    print("DATE_OF_INITIATION:",i[3])
                    print("EXPECTED ARRIVAL:",i[4])
                    print("COST_OF_PRODUCTION",i[5])
                    print("COST_OF_TRANSPORTATION:",i[6])
                    print("TOTAL COST:",i[7])
                    print("________________________________________________________________________________")
            else:
                pass
            C1=input("BACK TO MAIN MENU? Y/N ")
            if C1.upper()=='N':
                exit()
            else:
                pass
        else:
            print("INVALID PROJECT ID")
    else:
        SG=input("THERE AREN'T ANY PROJECTS IN PROGRESS WOULD YOU LIKE TO REGISTER A NEW ONE? (Y/N) ")
        if SG.upper()=='Y':
            ADD_TO_RESEARCH()
        else:
            pass
    
def DELETE_EMPLOYEE(): #ALLOWS THE ADMIN TO DELETE ENTRIES TO THE EMPLOYEE TABLE
    print("EMPLOYEES: ")
    A.execute("SELECT * from EMPLOYEE")
    EMP=A.fetchall()
    for i in EMP:
        print("EMPLOYEE_ID:",i[0])
        print("EMPLOYEE_NAME:",i[1])
        print("DESIGNATION:",i[2])
        print("SALARY:",i[3])
        print("DATE_OF_JOIN:",i[4])
        print("MEDICAL_ALLOWENCE",i[5])
        print("ACCOMODATION_ALLOWENCE:",i[6])
        print("CONTACT_NO:",i[7])
        print("GENDER:",i[8])
        print("DOB:",i[9])
        print("_____________________________________________________________________")
    if EMP!=[]:
        EID=getpass("ENTER THE ID NUMBER OF EMPLOYEE: ")
        Z="SELECT EMPLOYEE_ID from EMPLOYEE WHERE EMPLOYEE_ID='{}'".format(EID)
        A.execute(Z)
        EMPID=A.fetchall()
        print("")
        if EID in EMPID[0][0]:
            R=input("ARE YOU SURE? ")
            if R.upper()=='Y':
                SQL6="DELETE FROM EMPLOYEE WHERE EMPLOYEE_ID=('{}')".format(EID)
                A.execute(SQL6)
                con.commit()
                SQL68="DELETE FROM EMPLOYEE_USER WHERE EMPLOYEE_NUMBER=('{}')".format(EID)
                A.execute(SQL68)
                con.commit()
                print("SUCESSFULLY DELETED")
                print("")
                A.execute("SELECT * from EMPLOYEE")
                E=A.fetchall()
                for i in E:
                    print("EMPLOYEE_ID:",i[0])
                    print("EMPLOYEE_NAME:",i[1])
                    print("DESIGNATION:",i[2])
                    print("SALARY:",i[3])
                    print("DATE_OF_JOIN:",i[4])
                    print("MEDICAL_ALLOWENCE",i[5])
                    print("ACCOMODATION_ALLOWENCE:",i[6])
                    print("CONTACT_NO:",i[7])
                    print("GENDER:",i[8])
                    print("DOB:",i[9])
                    print("_____________________________________________________________________")
            else:
                pass
            C1=input("BACK TO MAIN MENU? Y/N ")
            if C1.upper()=='N':
                exit()
            else:
                pass
        else:
            print("INVALID EMPLOYEE ID")
    else:
        print("NO EMPLOYEE RECORDS AT THE MOMENT")
        X=input("DO YOU WISH TO ADD NEW EMPLOYEE RECORDS? (Y/N) ")
        if X.upper()=='Y':
            ADD_TO_EMPLOYEE()
        else:
            pass
    
def DELETE_CATALOGE(): #ALLOWS THE ADMIN TO DELETE ENTRIES TO THE CATALOGE TABLE
    print("PRODUCTS: ")
    A.execute("SELECT * from CATALOGE")
    CP=A.fetchall()
    for i in CP:
        print("PRODUCT_ID:",i[0])
        print("PRICE:",i[1])
        print("PRODUCT NAME:",i[2])
        print("________________________________________________________________________________")
    if CP!=[]:
        PN=getpass("ENTER THE PRODUCT ID: ")
        X="SELECT PRODUCT_ID from CATALOGE WHERE PRODUCT_ID='{}'".format(PN)
        A.execute(X)
        CPID=A.fetchall()
        print("")
        if PN in CPID[0][0]:
            E=input("ARE YOU SURE? (Y/N) ")
            if E.upper()=='Y':
                SQL7="DELETE FROM CATALOGE WHERE PRODUCT_ID='{}'".format(PN)
                A.execute(SQL7)
                con.commit()
                print("SUCESSFULLY DELETED")
                print("")
                A.execute("SELECT * from CATALOGE")
                AAA=A.fetchall()
                for i in AAA:
                    print("PRODUCT_ID:",i[0])
                    print("PRICE:",i[1])
                    print("PRODUCT NAME:",i[2])
                    print("________________________________________________________________________________")
            else:
                pass
            C1=input("BACK TO MAIN MENU? Y/N ")
            if C1.upper()=='N':
                exit()
            else:
                pass
        else:
            print("INVALID PRODUCT ID")
    else:
        Y=input("NO PRODUCTS LISTED FOR SALE WOULD YOU LIKE TO ADD NEW PRODUCTS? (Y/N) ")
        if Y.upper()=='Y':
            ADD_TO_CATALOGE()
        else:
            pass
    
def DELETE_CLIENTS_ADMIN(): #ALLOWS THE ADMIN TO DELETE ENTRIES TO THE CLIENTS TABLE BY ADMIN
    print("CLIENTS IN CONTACT: ")
    A.execute("SELECT * from CLIENTS")
    UCD=A.fetchall()
    A.execute("SELECT CLIENT_ID from CLIENTS")
    DCID=A.fetchall()
    print(UCD)
    print(DCID)
    if UCD!=[]:
        CN=getpass("ENTER THE CLIENT ID: ")
        qq="SELECT CLIENT_ID from CLIENTS WHERE CLIENT_ID='{}'".format(CN)
        A.execute(qq)
        DCID=A.fetchall()
        if CN in DCID[0][0]:
            U=input("ARE YOU SURE? (Y/N) ")
            print("")
            if U.upper()=='Y':
                SQL8="DELETE FROM CLIENTS WHERE CLIENT_ID='{}'".format(CN)
                A.execute(SQL8)
                con.commit()
                print("SUCESSFULLY DELETED")
                print("")
                A.execute("SELECT * from CLIENTS")
                print("________________")
                A.execute("SELECT * from CLIENTS")
                P=A.fetchall()
                for i in P:
                    print("CLIENT_ID:",i[0])
                    print("USERNAME:",i[1])
                    print("PASSWORD:",i[2])
                    print("CLIENT_NAME:",i[3])
                    print("CLIENT_CONTACT:",i[4])
                    print("__________________________________________________________________________________")
                print("")
            else:
                pass
            C1=input("BACK TO MAIN MENU? Y/N ")
            if C1.upper()=='N':
                exit()
            else:
                pass
        else:
            print("INVALID CLIENT ID")
    else:
        NCD=input("THERE ARE NO CLIENTS AT THE MOMENT WOULD YOU LIKE TO ADD A NEW CLIENT? (Y/N) ")
        if NCD.upper()=='Y':
            ADD_TO_CLIENT()
        else:
            pass
        
def DELETE_CLIENTS(): #ALLOWS THE ADMIN TO DELETE ENTRIES TO THE CLIENTS TABLE
    CN=getpass("ENTER THE CLIENT ID: ")
    qq="SELECT CLIENT_ID from CLIENTS WHERE CLIENT_ID='{}'".format(CN)
    A.execute(qq)
    DCID=A.fetchall()
    if CN in DCID[0][0]:
        U=input("ARE YOU SURE? (Y/N) ")
        print("")
        if U.upper()=='Y':
            SQL8="DELETE FROM CLIENTS WHERE CLIENT_ID='{}'".format(CN)
            A.execute(SQL8)
            con.commit()
            print("SUCESSFULLY DELETED")
            print("")
        else:
            pass
        C1=input("BACK TO MAIN MENU? Y/N ")
        if C1.upper()=='N':
            exit()
        else:
            pass
    else:
        print("INVALID CLIENT ID")
 
def CANCEL_ORDERS(): #ALLOWS THE USER TO DELETE ENTRIES TO THE SALES_TRANSACTIONS TABLE
    C_USERNAME=input("CONFIRM YOUR USERNAME: ")
    print("ORDERS PLACED: ")
    SQL3700=("SELECT * from SALES_TRANSACTIONS WHERE USER='{}'").format(C_USERNAME)
    A.execute(SQL3700)
    we=A.fetchall()
    for i in we:
        print("PRODUCT_ID",i[0])
        print("QUANTITY",i[1])
        print("COST_PER_UNIT",i[2])
        print("COMPANY_NAME",i[3])
        print("TRANSACTION_ID",i[4])
        print("TOTAL_PAYMENT",i[5])
        print("USERNAME",i[6])
        print("______________________________________________________________________")
    if we!=[]:
        TID=getpass("ENTER THE TRANSACTION ID: ")
        SQL3701=("SELECT TRANSACTION_ID from SALES_TRANSACTIONS WHERE TRANSACTION_ID='{}'").format(TID)
        A.execute(SQL3701)
        STID=A.fetchall()
        for i in STID:
            print("PRODUCT_ID",i[0])
            print("QUANTITY",i[1])
            print("COST_PER_UNIT",i[2])
            print("COMPANY_NAME",i[3])
            print("TRANSACTION_ID",i[4])
            print("TOTAL_PAYMENT",i[5])
            print("USERNAME",i[6])
            print("______________________________________________________________________")
        if TID in STID[0][0]:
            U=input("ARE YOU SURE? (Y/N) ")
            if U.upper()=='Y':
                SQL9="DELETE FROM SALES_TRANSACTIONS WHERE TRANSACTION_ID=('{}')".format(TID)
                A.execute(SQL9)
                con.commit()
                print("SUCESSFULLY DELETED")
                print("")
                SQL37009=("SELECT * from SALES_TRANSACTIONS WHERE USER='{}'").format(C_USERNAME)
                A.execute(SQL37009)
                we=A.fetchall()
                for i in we:
                    print("PRODUCT_ID",i[0])
                    print("QUANTITY",i[1])
                    print("COST_PER_UNIT",i[2])
                    print("COMPANY_NAME",i[3])
                    print("TRANSACTION_ID",i[4])
                    print("TOTAL_PAYMENT",i[5])
                    print("USERNAME",i[6])
                    print("______________________________________________________________________")
            else:
                pass
            C1=input("BACK TO MAIN MENU? Y/N ")
            if C1.upper()=='N':
                exit()
            else:
                pass
        else:
            print("INCORRECT ORDER NUMBER")
    else:
        F=input("THERE SEEMS THERE WERENT ANY RECORDED, WOULD YOU LIKE TO ADD THEM? (Y/N) ")
        if F=='Y':
            ADD_TO_SALES()
        else:
            pass

def DELETE_OPENING(): #ALLOWS THE ADMIN TO DELETE ENTRIES TO THE CAREERS TABLE
    print("RECRUITMENTS IN PROGRESS: ")
    A.execute("SELECT * from CAREERS")
    CA=A.fetchall()
    for i in CA:
        print("DESIGNATION:",i[0])
        print("SALARY OFFERED:",i[1])
        print("REQUIRED QUALIFICATION:",i[2])
        print("REQUIRED YEARS OF SERVICES:",i[3])
        print("_____________________________________________________________________")
    print("")
    if CA!=[]:
        DO=input("THE NAME OF OPENING TO BE DELETED: ")
        D1="SELECT DESIGNATION FROM CAREERS WHERE DESIGNATION='{}'".format(DO)
        A.execute(D1)
        DO1=A.fetchall()
        if DO in DO1[0][0]:
            SURE=input("ARE YOU SURE? (Y/N)")
            if SURE.upper()=='Y':
                SQL26="DELETE FROM CAREERS WHERE DESIGNATION=('{}')".format(DO)
                A.execute(SQL26)
                con.commit()
                print("SUCESSFULLY DELETED")
                print("")
                A.execute("SELECT * from CAREERS")
                CA=A.fetchall()
                for i in CA:
                    print("DESIGNATION:",i[0])
                    print("SALARY OFFERED:",i[1])
                    print("REQUIRED QUALIFICATION:",i[2])
                    print("REQUIRED YEARS OF SERVICES:",i[3])
                    print("_____________________________________________________________________")
            else:
                pass
            C1=input("BACK TO MAIN MENU? Y/N ")
            if C1.upper()=='N':
                exit()
            else:
                pass
        else:
            print("INVALID DESIGNATION ENTERED")
    else:
        IU=input("THERE AREN'T ANY POSTING AT THE MOMENT WOULD YOU LIKE TO ADD A NEW? (Y/N) ")
        if IU.upper()=='Y':
            ADD_TO_CAREERS()
        else:
            pass
        
def UPDATE_APPLICATIONS():
    print("ACTIVE APPLICATIONS")
    n=input("CONFIRM YOUR USER NAME: ")
    SQL79="SELECT * FROM APPLICATIONS WHERE USER='{}'".format(n)
    A.execute(SQL79)
    CAPP=A.fetchall()
    print(CAPP)
    if CAPP!=[]:
        print("UPDATE YOUR APPLICATION")
        print("MAIN MENU")
        print("1. UPDATE NAME")
        print("2. CONTACT INFORMATION")
        print("3. RETRACT APPLICATION")
        Q=int(input("WHAT WOULD YOU LIKE TO UPDATE ABOUT YOUR APPLICATION? "))
        if Q==1:
            N1=input("ENTER THE UPDATED NAME: ")
            SURE=input("ARE YOU SURE? (Y/N)")
            if SURE.upper()=='Y':
                SQL26="UPDATE APPLICATIONS SET NAME='{}' WHERE USER=('{}')".format(N1,n)
                A.execute(SQL26)
                con.commit()
                print("SUCESSFULLY UPDATED!")
                print("")
                SQL79="SELECT * FROM APPLICATIONS WHERE USER='{}'".format(n)
                A.execute(SQL79)
                CAPP=A.fetchall()
                print(CAPP)
            else:
                print("TERMINATED")
        elif Q==2:
            N2=input("ENTER THE UPDATED CONTACT INFO: ")
            SURE=input("ARE YOU SURE? (Y/N)")
            if SURE.upper()=='Y':
                SQL261="UPDATE APPLICATIONS SET CONTACT_INFO='{}' WHERE USER='{}'".format(N2,n)
                A.execute(SQL261)
                con.commit()
                print("SUCESSFULLY UPDATED!")
                A.execute("SELECT * from APPLICATIONS")
                print(A.fetchall())
            else:
                print("TERMINATED")
        elif Q==3:
            SQL98="DELETE FROM APPLICATIONS WHERE USER=('{}')".format(n)
            A.execute(SQL98)
            con.commit()
            print("SUCESSFULLY DELETED")
    else:
        print("NO APPLICATIONS AT THE MOMENT")
        I=input("DO YOU WANT TO SUBMIT A NEW FORM?")
        if I.upper()=='Y':
            ADD_TO_APPLICATIONS()
        else:
            exit()

def UPDATE_EMPLOYEE_DETAILS(): #ALLOWS THE ADMIN TO UPDATE ENTRIES TO THE EMPLOYEE TABLE
    print("EMPLOYEES: ")
    A.execute("SELECT * from EMPLOYEE")
    EMP=A.fetchall()
    for i in EMP:
        print("EMPLOYEE_ID:",i[0])
        print("EMPLOYEE_NAME:",i[1])
        print("DESIGNATION:",i[2])
        print("SALARY:",i[3])
        print("DATE_OF_JOIN:",i[4])
        print("MEDICAL_ALLOWENCE",i[5])
        print("ACCOMODATION_ALLOWENCE:",i[6])
        print("CONTACT_NO:",i[7])
        print("GENDER:",i[8])
        print("DOB:",i[9])
        print("_____________________________________________________________________")
    if EMP!=[]:
        print("")
        print("1. PROMOTE EMPLOYEE")
        print("2. SALARY HIKE")
        print("3. UPDATE CONTACT INFORMATION")
        print("4. SALARY DECREMENT")
        D=int(input("ENTER YOUR CHOICE: "))
        if D==1:
            EN=getpass("ENTER EMPLOYEE ID: ")
            V="SELECT EMPLOYEE_ID from EMPLOYEE WHERE EMPLOYEE_ID='{}'".format(EN)
            A.execute(V)
            EMPID=A.fetchall()
            if EN in EMPID[0][0]:
                ND=input("ENTER NEW DESIGNATION: ")
                NS=float(input("ENTER NEW SALARY: "))
                MED=NS*0.2
                AC=NS*0.1
                SQL10="UPDATE EMPLOYEE SET DESIGNATION='{}',SALARY='{}',MEDICAL_ALLOWENCE='{}',ACCOMODATION_ALLOWENCE='{}' WHERE EMPLOYEE_ID='{}'".format(ND,NS,MED,AC,EN)
                A.execute(SQL10)
                con.commit()
                print("")
                A.execute("SELECT * from EMPLOYEE")
                E=A.fetchall()
                for i in E:
                    print("EMPLOYEE_ID:",i[0])
                    print("EMPLOYEE_NAME:",i[1])
                    print("DESIGNATION:",i[2])
                    print("SALARY:",i[3])
                    print("DATE_OF_JOIN:",i[4])
                    print("MEDICAL_ALLOWENCE",i[5])
                    print("ACCOMODATION_ALLOWENCE:",i[6])
                    print("CONTACT_NO:",i[7])
                    print("GENDER:",i[8])
                    print("DOB:",i[9])
                    print("_____________________________________________________________________")
                C1=input("BACK TO MAIN MENU? Y/N ")
                if C1.upper()=='N':
                    exit()
                else:
                    pass
            else:
                print("INVALID EMPLOYEE ID")
        elif D==2:
            EN=getpass("ENTER THE EMPLOYEE NO")
            V="SELECT EMPLOYEE_ID from EMPLOYEE WHERE EMPLOYEE_ID='{}'".format(EN)
            A.execute(V)
            EMPID=A.fetchall()
            if EN in EMPID[0][0]:
                NEW_SALARY=int(input("ENTER THE % SALARY HIKE: "))
                SALARY_DECIMAL=int(NEW_SALARY)/100
                SQL11="UPDATE EMPLOYEE SET SALARY=SALARY+SALARY*'{}',ACCOMODATION_ALLOWENCE=ACCOMODATION_ALLOWENCE+ACCOMODATION_ALLOWENCE*'{}',MEDICAL_ALLOWENCE=MEDICAL_ALLOWENCE+MEDICAL_ALLOWENCE*'{}' WHERE EMPLOYEE_ID='{}'".format(SALARY_DECIMAL,SALARY_DECIMAL,SALARY_DECIMAL,EN)
                A.execute(SQL11)
                con.commit()
                print("")
                print("SUCESSFULLY UPDATED")
                print("")
                A.execute("SELECT * from EMPLOYEE")
                E1=A.fetchall()
                for i in E1:
                    print("EMPLOYEE_ID:",i[0])
                    print("EMPLOYEE_NAME:",i[1])
                    print("DESIGNATION:",i[2])
                    print("SALARY:",i[3])
                    print("DATE_OF_JOIN:",i[4])
                    print("MEDICAL_ALLOWENCE",i[5])
                    print("ACCOMODATION_ALLOWENCE:",i[6])
                    print("CONTACT_NO:",i[7])
                    print("GENDER:",i[8])
                    print("DOB:",i[9])
                    print("_____________________________________________________________________")
                C1=input("BACK TO MAIN MENU? Y/N ")
                if C1.upper()=='N':
                    exit()
                else:
                    pass
        elif D==3:
            EN=getpass("ENTER THE EMPLOYEE NO")
            V="SELECT EMPLOYEE_ID from EMPLOYEE WHERE EMPLOYEE_ID='{}'".format(EN)
            A.execute(V)
            EMPID=A.fetchall()
            if EN in EMPID[0][0]:
                NEW_CONTACT=input("ENTER THE NEW CONTACT INFO (EMAIL/PH NUMBER): ")
                print("")
                SQL11="UPDATE EMPLOYEE SET CONTACT_NO='{}' WHERE EMPLOYEE_NAME='{}'".format(NEW_CONTACT,EN)
                A.execute(SQL11)
                con.commit()
                print("SUCESSFULLY UPDATED")
                print("")
                A.execute("SELECT * from EMPLOYEE")
                E=A.fetchall()
                for i in E:
                    print("EMPLOYEE_ID:",i[0])
                    print("EMPLOYEE_NAME:",i[1])
                    print("DESIGNATION:",i[2])
                    print("SALARY:",i[3])
                    print("DATE_OF_JOIN:",i[4])
                    print("MEDICAL_ALLOWENCE",i[5])
                    print("ACCOMODATION_ALLOWENCE:",i[6])
                    print("CONTACT_NO:",i[7])
                    print("GENDER:",i[8])
                    print("DOB:",i[9])
                    print("_____________________________________________________________________")
                C1=input("BACK TO MAIN MENU? Y/N ")
                if C1.upper()=='N':
                    exit()
                else:
                    pass
            else:
                print("INVALID EMPLOYEE ID")
        elif D==4:
            EN=getpass("ENTER THE EMPLOYEE NO")
            V="SELECT EMPLOYEE_ID from EMPLOYEE WHERE EMPLOYEE_ID='{}'".format(EN)
            A.execute(V)
            EMPID=A.fetchall()
            if EN in EMPID[0][0]:
                NEW_SALARY=int(input("ENTER THE % SALARY DECREASE: "))
                SALARY_DECIMAL=int(NEW_SALARY)/100
                SQL111="UPDATE EMPLOYEE SET SALARY=SALARY-SALARY*'{}',ACCOMODATION_ALLOWENCE=ACCOMODATION_ALLOWENCE-ACCOMODATION_ALLOWENCE*'{}',MEDICAL_ALLOWENCE=MEDICAL_ALLOWENCE-MEDICAL_ALLOWENCE*'{}' WHERE EMPLOYEE_ID='{}'".format(SALARY_DECIMAL,SALARY_DECIMAL,SALARY_DECIMAL,EN)
                A.execute(SQL111)
                con.commit()
                print("")
                print("SUCESSFULLY UPDATED")
                print("")
                A.execute("SELECT * from EMPLOYEE")
                E11=A.fetchall()
                for i in E11:
                    print("EMPLOYEE_ID:",i[0])
                    print("EMPLOYEE_NAME:",i[1])
                    print("DESIGNATION:",i[2])
                    print("SALARY:",i[3])
                    print("DATE_OF_JOIN:",i[4])
                    print("MEDICAL_ALLOWENCE",i[5])
                    print("ACCOMODATION_ALLOWENCE:",i[6])
                    print("CONTACT_NO:",i[7])
                    print("GENDER:",i[8])
                    print("DOB:",i[9])
                    print("_____________________________________________________________________")
                C1=input("BACK TO MAIN MENU? Y/N ")
                if C1.upper()=='N':
                    exit()
                else:
                    pass
    else:
        print("NO EMPLOYEE RECORDS AT THE MOMENT")
        X=input("DO YOU WISH TO ADD NEW EMPLOYEE RECORDS? (Y/N) ")
        if X.upper()=='Y':
            ADD_TO_EMPLOYEE()
        else:
            pass

def UPDATE_PRODUCT_INFO(): #ALLOWS THE ADMIN TO UPDATE ENTRIES TO THE CATALOGE TABLE
    print("PRODUCTS: ")
    A.execute("SELECT * from CATALOGE")
    CP=A.fetchall()
    for i in CP:
        print("PRODUCT_ID:",i[0])
        print("PRICE:",i[1])
        print("PRODUCT NAME:",i[2])
        print("________________________________________________________________________________")
    if CP!=[]:
        print("1. UPDATE PRODUCT PRICE: ")
        print("2. UPDATE PRODUCT NAME: ")
        D=int(input("ENTER YOUR CHOICE: "))
        if D==1:
            PNA=getpass("ENTER THE PRODUCT ID: ")
            Y="SELECT PRODUCT_ID from CATALOGE WHERE PRODUCT_ID='{}'".format(PNA)
            A.execute(Y)
            CPID=A.fetchall()
            if PNA in CPID[0][0]:
                NPP=input("ENTER THE NEW PRODUCT PRICE: ")
                SQL13="UPDATE CATALOGE SET PRICE='{}' WHERE PRODUCT_ID='{}'".format(NPP,PNA)
                A.execute(SQL13)
                con.commit()
                print("")
                print("SUCESSFULLY UPDATED")
                print("")
                A.execute("SELECT * from CATALOGE")
                CP=A.fetchall()
                for i in CP:
                    print("PRODUCT_ID:",i[0])
                    print("PRICE:",i[1])
                    print("PRODUCT NAME:",i[2])
                    print("________________________________________________________________________________")
                C1=input("BACK TO MAIN MENU? Y/N ")
                if C1.upper()=='N':
                    exit()
                else:
                    pass
            else:
                print("INVALID PRODUCT_ID")
        elif D==2:
            PD=getpass("ENTER THE PRODUCT ID: ")
            Y="SELECT PRODUCT_ID from CATALOGE WHERE PRODUCT_ID='{}'".format(PD)
            A.execute(Y)
            CPID=A.fetchall()
            if PD in CPID[0][0]:
                NPN=input("ENTER THE NEW PRODUCT NAME: ")
                SQL14="UPDATE CATALOGE SET PRODUCT_NAME='{}' WHERE PRODUCT_ID='{}'".format(NPN,PD)
                A.execute(SQL14)
                con.commit()
                print("")
                print("SUCESSFULLY UPDATED")
                print("")
                A.execute("SELECT * from CATALOGE")
                CP=A.fetchall()
                for i in CP:
                    print("PRODUCT_ID:",i[0])
                    print("PRICE:",i[1])
                    print("PRODUCT NAME:",i[2])
                    print("________________________________________________________________________________")
                C1=input("BACK TO MAIN MENU? Y/N ")
                if C1.upper()=='N':
                    exit()
                else:
                    pass
            else:
                print("INVALID PRODUCT_ID")
        else:
            print("INVALID COMMAND")
    else:
        Y=input("NO PRODUCTS LISTED FOR SALE WOULD YOU LIKE TO ADD NEW PRODUCTS? (Y/N) ")
        if Y.upper()=='Y':
            ADD_TO_CATALOGE()
        else:
            pass
        
def UPDATE_PROJECT_INFO(): #ALLOWS THE ADMIN TO UPDATE ENTRIES TO THE PROJECTS TABLE
    print("PROJECTS: ")
    A.execute("SELECT * from PROJECTS")
    PI=A.fetchall()
    for i in PI:
        print("PROJECT_ID:",i[0])
        print("PROJECT_NAME:",i[1])
        print("COUNTRY_OF_ORIGIN:",i[2])
        print("DATE_OF_INITIATION:",i[3])
        print("EXPECTED ARRIVAL:",i[4])
        print("COST_OF_PRODUCTION",i[5])
        print("COST_OF_TRANSPORTATION:",i[6])
        print("TOTAL COST:",i[7])
        print("________________________________________________________________________________")
    if PI!=[]:
        print("")
        print("1. UPDATE PROJECT_NAME")
        print("2. UPDATE COUNTRY OF ORIGIN")
        print("3. UPDATE DATE_OF_INITIATION")
        print("4. UPDATE EXPECTED ARRIVAL")
        print("5. UPDATE EXPENSES")
        CH=int(input("ENTER YOUR CHOICE: "))
        if CH==1:
            PROJID=getpass("ENTER PROJECT ID: ")
            O="SELECT PROJECT_ID from PROJECTS WHERE PROJECT_ID='{}'".format(PROJID)
            A.execute(O)
            PID=A.fetchall()
            if PROJID in PID[0][0]:
                N=input("ENTER THE NEW PROJECT NAME: ")
                SQL16="UPDATE PROJECTS SET PROJECT_NAME='{}' WHERE PROJECT_ID='{}'".format(N,PROJID)
                A.execute(SQL16)
                con.commit()
                print("")
                print("SUCESSFULLY UPDATED")
                print("")
                A.execute("SELECT * from PROJECTS")
                P=A.fetchall()
                for i in P:
                    print("PROJECT_ID:",i[0])
                    print("PROJECT_NAME:",i[1])
                    print("COUNTRY_OF_ORIGIN:",i[2])
                    print("DATE_OF_INITIATION:",i[3])
                    print("EXPECTED ARRIVAL:",i[4])
                    print("COST_OF_PRODUCTION",i[5])
                    print("COST_OF_TRANSPORTATION:",i[6])
                    print("TOTAL COST:",i[7])
                    print("________________________________________________________________________________")
                C1=input("BACK TO MAIN MENU? Y/N ")
                if C1.upper()=='N':
                    exit()
                else:
                    pass
            else:
                print("INVALID PROJECT ID")
        elif CH==2:
            P=getpass("ENTER PROJECT ID: ")
            O="SELECT PROJECT_ID from PROJECTS WHERE PROJECT_ID='{}'".format(P)
            A.execute(O)
            PID=A.fetchall()
            if P in PID[0][0]:
                COO=input("ENTER THE NEW COUNTRY OF ORIGIN: ")
                SQL17="UPDATE PROJECTS SET COUNTRY_OF_ORIGIN='{}' WHERE PROJECT_ID='{}'".format(COO,P)
                A.execute(SQL17)
                con.commit()
                print("")
                print("SUCESSFULLY UPDATED")
                print("")
                A.execute("SELECT * from PROJECTS")
                P=A.fetchall()
                for i in P:
                    print("PROJECT_ID:",i[0])
                    print("PROJECT_NAME:",i[1])
                    print("COUNTRY_OF_ORIGIN:",i[2])
                    print("DATE_OF_INITIATION:",i[3])
                    print("EXPECTED ARRIVAL:",i[4])
                    print("COST_OF_PRODUCTION",i[5])
                    print("COST_OF_TRANSPORTATION:",i[6])
                    print("TOTAL COST:",i[7])
                    print("________________________________________________________________________________")
                C1=input("BACK TO MAIN MENU? Y/N ")
                if C1.upper()=='N':
                    exit()
                else:
                    pass
            else:
                print("INVALID PROJECT ID")
        elif CH==3:
            P_ID=getpass("ENTER THE PROJECT ID: ")
            O="SELECT PROJECT_ID from PROJECTS WHERE PROJECT_ID='{}'".format(P_ID)
            A.execute(O)
            PID=A.fetchall()
            if P_ID in PID[0][0]:
                DOI=input("THE NEW DATE OF INITIATION (DD/MM/YYYY): ")
                SQL18="UPDATE PROJECTS SET DATE_OF_INITIATION='{}' WHERE PROJECT_ID='{}'".format(DOI,P_ID)
                A.execute(SQL18)
                con.commit()
                print("")
                print("SUCESSFULLY UPDATED")
                print("")
                A.execute("SELECT * from PROJECTS")
                P=A.fetchall()
                for i in P:
                    print("PROJECT_ID:",i[0])
                    print("PROJECT_NAME:",i[1])
                    print("COUNTRY_OF_ORIGIN:",i[2])
                    print("DATE_OF_INITIATION:",i[3])
                    print("EXPECTED ARRIVAL:",i[4])
                    print("COST_OF_PRODUCTION",i[5])
                    print("COST_OF_TRANSPORTATION:",i[6])
                    print("TOTAL COST:",i[7])
                    print("________________________________________________________________________________")
                C1=input("BACK TO MAIN MENU? Y/N ")
                if C1.upper()=='N':
                    exit()
                else:
                    pass
            else:
                print("INVALID PROJECT ID")
        elif CH==4:
            PRO_ID=getpass("ENTER THE PROJECT ID: ")
            O="SELECT PROJECT_ID from PROJECTS WHERE PROJECT_ID='{}'".format(PRO_ID)
            A.execute(O)
            PID=A.fetchall()
            if PRO_ID in PID[0][0]:
                EA=input("THE NEW DATE OF LAUNCH (DD/MM/YYYY):")
                SQL19="UPDATE PROJECTS SET EXPECTED_ARRIVAL='{}' WHERE PROJECT_ID='{}'".format(EA,PRO_ID)
                A.execute(SQL19)
                con.commit()
                print("")
                print("SUCESSFULLY UPDATED")
                print("")
                A.execute("SELECT * from PROJECTS")
                P=A.fetchall()
                for i in P:
                    print("PROJECT_ID:",i[0])
                    print("PROJECT_NAME:",i[1])
                    print("COUNTRY_OF_ORIGIN:",i[2])
                    print("DATE_OF_INITIATION:",i[3])
                    print("EXPECTED ARRIVAL:",i[4])
                    print("COST_OF_PRODUCTION",i[5])
                    print("COST_OF_TRANSPORTATION:",i[6])
                    print("TOTAL COST:",i[7])
                    print("________________________________________________________________________________")
                C1=input("BACK TO MAIN MENU? Y/N ")
                if C1.upper()=='N':
                    exit()
                else:
                    pass
            else:
                print("INVALID PROJECT ID")
        elif CH==5:
            PR_ID=getpass("ENTER THE PROJECT ID: ")
            O="SELECT PROJECT_ID from PROJECTS WHERE PROJECT_ID='{}'".format(PR_ID)
            A.execute(O)
            PID=A.fetchall()
            if PR_ID in PID[0][0]:
                COP=float(input("ENTER THE NEW COST OF PRODUCTION: "))
                C1=float(input("ENTER THE TRANPORTATION COST: "))
                T1=float(C1+COP)
                SQL20="UPDATE PROJECTS SET COST_OF_PRODUCTION='{}',COST_OF_TRANSPORT='{}',TOTAL_COST='{}' WHERE PROJECT_ID='{}'".format(COP,C1,T1,PR_ID)
                A.execute(SQL20)
                con.commit()
                print("")
                print("SUCESSFULLY UPDATED")
                print("")
                A.execute("SELECT * from PROJECTS")
                P=A.fetchall()
                for i in P:
                    print("PROJECT_ID:",i[0])
                    print("PROJECT_NAME:",i[1])
                    print("COUNTRY_OF_ORIGIN:",i[2])
                    print("DATE_OF_INITIATION:",i[3])
                    print("EXPECTED ARRIVAL:",i[4])
                    print("COST_OF_PRODUCTION",i[5])
                    print("COST_OF_TRANSPORTATION:",i[6])
                    print("TOTAL COST:",i[7])
                    print("________________________________________________________________________________")
                C1=input("BACK TO MAIN MENU? Y/N ")
                if C1.upper()=='N':
                    exit()
                else:
                    pass
            else:
                print("INVALID PROJECT ID")
            C1=input("BACK TO MAIN MENU? Y/N ")
            if C1.upper()=='N':
                exit()
            else:
                pass
        else:
            print("INVALID COMMAND")
    else:
        SG=input("THERE AREN'T ANY PROJECTS IN PROGRESS WOULD YOU LIKE TO REGISTER A NEW ONE? (Y/N) ")
        if SG.upper()=='Y':
            ADD_TO_RESEARCH()
        else:
            pass
    
def UPDATE_CLIENT_DETAILS(): #ALLOWS THE ADMIN TO UPDATE ENTRIES TO THE CLIENTS TABLE
    print("CLIENTS: ")
    A.execute("SELECT * from CLIENTS")
    UCD=A.fetchall()
    print(UCD)
    if UCD!=[]:
        print("1. UPDATE CLIENT NAME")
        print("2. UPDATE CLIENT CONTACT_NUMBER")
        CHO=int(input("ENTER YOUR CHOICE: "))
        if CHO==1:
            CLN_ID=getpass("ENTER THE CLIENT ID: ")
            I="SELECT CLIENT_ID from CLIENTS WHERE CLIENT_ID='{}'".format(CLN_ID)
            A.execute(I)
            UCID=A.fetchall()
            print(UCID[0][0])
            if CLN_ID in UCID[0][0]:
                CLN=getpass("ENTER THE NEW CLIENT NAME: ")
                SQL37="UPDATE CLIENTS SET CLIENT_NAME='{}' WHERE CLIENT_ID='{}'".format(CLN,CLN_ID)
                A.execute(SQL37)
                con.commit()
                print("")
                print("SUCESSFULLY UPDATED")
                print("")
                A.execute("SELECT * from CLIENTS")
                print(A.fetchall())
                C1=input("BACK TO MAIN MENU? Y/N ")
                if C1.upper()=='N':
                    exit()
                else:
                    pass
            else:
                print("INVALID CLIENT ID")
        elif CHO==2:
            CLN_ID=getpass("ENTER THE CLIENT ID: ")
            I="SELECT CLIENT_ID from CLIENTS WHERE CLIENT_ID='{}'".format(CLN_ID)
            A.execute(I)
            UCID=A.fetchall()
            if CLN_ID in UCID[0][0]:
                CLN=input("ENTER THE NEW CLIENT NUMBER: ")
                SQL23="UPDATE CLIENTS SET CONTACT_NUMBER='{}' WHERE CLIENT_ID='{}'".format(CLN,CLN_ID)
                A.execute(SQL23)
                con.commit()
                print("")
                print("SUCESSFULLY UPDATED")
                print("")
                A.execute("SELECT * from CLIENTS")
                print(A.fetchall())
                C1=input("BACK TO MAIN MENU? Y/N ")
                if C1.upper()=='N':
                    exit()
                else:
                    pass
            else:
                print("INVALID CLIENT ID")
        else:
            print("INVALID COMMAND")
    else:
        NCD=input("THERE ARE NO CLIENTS AT THE MOMENT WOULD YOU LIKE TO ADD A NEW CLIENT? (Y/N) ")
        if NCD.upper()=='Y':
            ADD_TO_CLIENT()
        else:
            pass

def UPDATE_SALES(): #ALLOWS THE USER TO UPDATE ENTRIES TO THE SALES_TRANSACTIONS TABLE
    CNM=input("ENTER YOUR COMPANY NAME: ")
    SQL36=("SELECT * from SALES_TRANSACTIONS WHERE COMPANY_NAME='{}'").format(CNM)
    A.execute(SQL36)
    ST=A.fetchall() 
    for i in ST:
        print("PRODUCT_ID",i[0])
        print("QUANTITY",i[1])
        print("COST_PER_UNIT",i[2])
        print("COMPANY_NAME",i[3])
        print("TRANSACTION_ID",i[4])
        print("TOTAL_PAYMENT",i[5])
        print("USERNAME",i[6])
        print("______________________________________________________________________")
    if ST!=[]:
        TRID=getpass("ENTER THE ORDER ID: ")
        SQL36=("SELECT * from SALES_TRANSACTIONS WHERE TRANSACTION_ID='{}'").format(TRID)
        A.execute(SQL36)
        ST=A.fetchall()
        for i in ST:
            print("PRODUCT_ID",i[0])
            print("QUANTITY",i[1])
            print("COST_PER_UNIT",i[2])
            print("COMPANY_NAME",i[3])
            print("TRANSACTION_ID",i[4])
            print("TOTAL_PAYMENT",i[5])
            print("USERNAME",i[6])
            print("______________________________________________________________________")
        S=list(ST)
        if TRID==S[0][4]:
            print("YOUR ORDERS: ")
            print("1. UPDATE QUANTITY")
            print("2. UPDATE PRODUCT")
            CC=int(input("ENTER YOUR CHOICE: "))
            if CC==1:
                Q=int(input("ENTER THE NEW QUANTITY: "))
                PPU=int(S[0][2])
                TP=(Q*PPU)
                SQL24="UPDATE SALES_TRANSACTIONS SET QUANTITY='{}',TOTAL_PAYMENT='{}' WHERE TRANSACTION_ID='{}'".format(Q,TP,TRID)
                A.execute(SQL24)
                con.commit()
                print("")
                print("SUCESSFULLY UPDATED")
                print("")
                SQL3611=("SELECT * from SALES_TRANSACTIONS WHERE TRANSACTION_ID='{}'").format(TRID)
                A.execute(SQL3611)
                we=A.fetchall()
                for i in we:
                    print("PRODUCT_ID",i[0])
                    print("QUANTITY",i[1])
                    print("COST_PER_UNIT",i[2])
                    print("COMPANY_NAME",i[3])
                    print("TRANSACTION_ID",i[4])
                    print("TOTAL_PAYMENT",i[5])
                    print("USERNAME",i[6])
                    print("______________________________________________________________________")
                C1=input("BACK TO MAIN MENU? Y/N ")
                if C1.upper()=='N':
                    exit()
                else:
                    pass
            elif CC==2:
                A.execute("SELECT * FROM CATALOGE")
                Q=A.fetchall()
                for i in Q:
                    print("PRODUCT_ID:",i[0])
                    print("PRICE:",i[1])
                    print("PRODUCT NAME:",i[2])
                    print("________________________________________________________________________________")
                NP=input("ENTER THE ID OF THE NEW PRODUCT TO BE ORDERED: ")
                PPU=int(S[0][2])
                TP=(int(S[0][1])*int(PPU))
                SQL39="UPDATE SALES_TRANSACTIONS SET PRODUCT_ID='{}',TOTAL_PAYMENT='{}' WHERE TRANSACTION_ID='{}'".format(NP,TP,TRID)
                A.execute(SQL39)
                con.commit()
                print("")
                print("SUCESSFULLY UPDATED")
                print("")
                SQL3622=("SELECT * from SALES_TRANSACTIONS WHERE TRANSACTION_ID='{}'").format(TRID)
                A.execute(SQL3622)
                we=A.fetchall()
                for i in we:
                    print("PRODUCT_ID",i[0])
                    print("QUANTITY",i[1])
                    print("COST_PER_UNIT",i[2])
                    print("COMPANY_NAME",i[3])
                    print("TRANSACTION_ID",i[4])
                    print("TOTAL_PAYMENT",i[5])
                    print("USERNAME",i[6])
                    print("______________________________________________________________________")
            else:
                print("INVALID COMMAND!")
    else:
        F=input("THERE SEEMS THERE WERENT ANY RECORDED, WOULD YOU LIKE TO ADD THEM? (Y/N) ")
        if F.upper()=='Y':
            ADD_TO_SALES()
        else:
            pass
    C1=input("BACK TO MAIN MENU? Y/N ")
    if C1.upper()=='N':
        exit()
    else:
        pass
            
def UPDATE_CAREERS(): #ALLOWS THE ADMIN TO UPDATE ENTRIES TO THE CAREERS TABLE
    print("CAREERS: ")
    A.execute("SELECT * from CAREERS")
    CA=A.fetchall()
    for i in CA:
        print("DESIGNATION:",i[0])
        print("SALARY OFFERED:",i[1])
        print("REQUIRED QUALIFICATION:",i[2])
        print("REQUIRED YEARS OF SERVICES:",i[3])
        print("_____________________________________________________________________")
    if CA!=[]:
        DES=input("ENTER THE DESIGNATION ")
        U="SELECT DESIGNATION from CAREERS WHERE DESIGNATION='{}'".format(DES)
        A.execute(U)
        CA=A.fetchall()
        if DES in CA[0][0]:
            print("1. UPDATE SALARY OFFERED")
            print("2. UPDATE THE REQUIRED QUALIFICATION")
            print("3. UPDATE THE REQUIRED YEARS OF EXPERIANCE")
            CHO=int(input("ENTER YOUR CHOICE: "))
            if CHO==1:
                SAL=input("ENTER THE NEW SALARY OFFERED: ")
                SQL27="UPDATE CAREERS SET SALARY='{}' WHERE DESIGNATION='{}'".format(SAL,DES)
                A.execute(SQL27)
                con.commit()
                print("")
                print("SUCESSFULLY UPDATED")
                print("")
                A.execute("SELECT * from CAREERS")
                CA=A.fetchall()
                for i in CA:
                    print("DESIGNATION:",i[0])
                    print("SALARY OFFERED:",i[1])
                    print("REQUIRED QUALIFICATION:",i[2])
                    print("REQUIRED YEARS OF SERVICES:",i[3])
                    print("_____________________________________________________________________")
                C1=input("BACK TO MAIN MENU? Y/N ")
                if C1.upper()=='N':
                   exit()
                else:
                    pass
            elif CHO==2:
                REQ=input("ENTER THE NEW REQUIRED QUALIFICATION: ")
                SQL28="UPDATE CAREERS SET REQUIRED_QUALIFICATION='{}' WHERE DESIGNATION='{}'".format(REQ,DES)
                A.execute(SQL28)
                con.commit()
                print("")
                print("SUCESSFULLY UPDATED")
                print("")
                A.execute("SELECT * from CAREERS")
                CA=A.fetchall()
                for i in CA:
                    print("DESIGNATION:",i[0])
                    print("SALARY OFFERED:",i[1])
                    print("REQUIRED QUALIFICATION:",i[2])
                    print("REQUIRED YEARS OF SERVICES:",i[3])
                    print("_____________________________________________________________________")
                C1=input("BACK TO MAIN MENU? Y/N ")
                if C1.upper()=='N':
                    exit()
                else:
                    pass
            elif CHO==3:
                RYOE=input("ENTER THE NEW REQUIRED YEARS OF EXPERIANCE: ")
                SQL29="UPDATE CAREERS SET REQUIRED_YEARS_OF_EXPERIANCE='{}' WHERE DESIGNATION='{}'".format(RYOE,DES)
                A.execute(SQL29)
                con.commit()
                print("")
                print("SUCESSFULLY UPDATED")
                print("")
                A.execute("SELECT * from CAREERS")
                CA=A.fetchall()
                for i in CA:
                    print("DESIGNATION:",i[0])
                    print("SALARY OFFERED:",i[1])
                    print("REQUIRED QUALIFICATION:",i[2])
                    print("REQUIRED YEARS OF SERVICES:",i[3])
                    print("_____________________________________________________________________")
                C1=input("BACK TO MAIN MENU? Y/N ")
                if C1.upper()=='N':
                    exit()
                else:
                    pass
            else:
                print("INVALID COMMAND")
    else:
        IU=input("THERE AREN'T ANY POSTING AT THE MOMENT WOULD YOU LIKE TO ADD A NEW? (Y/N) ")
        if IU.upper()=='Y':
            ADD_TO_CAREERS()
        else:
            pass
        
def BOOT_UP(): #PLAYS THE SOUND FOR BOOTING UP ADMIN MENU
    from pygame import mixer
    mixer.init()
    mixer.music.load('J1.mp3')
    mixer.music.play()
        
def LOGO(): #PRINTS THE LOGO FOR THE COMPANY
    print("""                                                                        .;:'                                                   
                                                                           .oO:                                                   
                                                      ........              .o:                                                   
                                                 .;:cldkkkkxdol;.           .l;                                                   
                                               .ck00kOOO00000000xl;.        .l;                                                   
                                              'oxxxkxkO00000000000kc.       'd:                                                   
                                          .,';cllll;...';:ldxk0000Okl.     ,kO:                                                   
                                         'x0O00000O:        .cO00000k:.    c00:                                                   
                                         ;O000OOkko.        .d000O0kooc.   c00:                                                   
                                        .ckkkxxxxdlc:,'..   ,k00000O0ko'  .o0O:                                                   
                                        'xOO0Odccccc:;,'.   cOkO000kkOl.  'xO0d.                                                  
                                       .;xOO0k,            .x0OOOOOkdo,. .;xk0k,                                                  
     .;dxxddxddxxxddxxdddxxddxddddddddddxkO00Odcclllllllooox00000000Okdxxxxkk00kddddddddddddddddddddxdddxxdddddddxxddxxdxdxd,     
      .:k00000000000000000000000000000000000000000000000000000000000000000OkxO00000000000000000000000000000000000000000000x;      
        'd00000000000Oxl:;;;;;;;;;;;;;;;;;:ok0OOO00000000000000000000000000OkOOo;;;;;;;;;;;;;;;;;;;;;;;;;;cdk00000000000Oo.       
         .ck0000000000Okdc;.                .'..:k000000000000000OOkO000000000O,                      .':lxO00000000000x;.        
           'd0000OdoxO00000kdc;.                 ;dolcd00000000OxdxkkO00000000O,                  .':lxO0000000OO0000Oo.          
            .ck000k:.';ldO00000Oxl;'.                .ldx000000xdkOOOkOOdd00OOk,              .':lxO0000000Odlcx0000k:.           
              ,d000Ol.   .;ldk00000Oxl:'.     ..';:;';oc:ok0000xccd00Od,..cxkkko'         .';lxO0000000Odl;..,dO00Oo'             
               .lO000x;      .,cok00000Oxoc;;cxO0kl,....ddcx00OdoxO0d:.    ,xOkkxl;'. ..;lxO0000000Oxl;.   .:k000k:.              
                 ,x000Ol.        .,coxO0OOOOOOxl;.      ;OxcxkldOKOl.       .;dOOkkkxddk0000000Odl;.      'dO000d'                
                  .lO000x,           .lOOOkOkc.          ;xxl:oOxo;.          .o0Oxkkkdk000Oxl;'.       .:k000Oc.                 
                    ;x000Oc.         ,dO0OxOo.            .lkOOc.              ,k0kkOkdxko:'.          .oO00Od'                   
                     .oO000d'       .oO00kxx;              'dko.               .ckxxkkxxo,            .lxxxd:.                    
                       ';;;,.       ..'''''..               ...                 .........        ..   ......                      
                     'clool;. .:c:c,. .;cloo:. .,cc:;. .:oc.  .':cc::lc''cl;. ,c:::. 'cl;.   .co;;looooooooo;.                    
                     c0x::lkx',Ox'... ,Ox::oOk,.dO:...  c0c  'dko:'..cx,.dO, .d0:... .xKOo'  .o0; .;;:xOo:;cc.                    
                    .o0:  'kO:c0x;,c:.:Oc .:OOc,xOc,:l;'oOc.,x0l.     ..,xO,.'dOc,:l;,k0ookc..oO;    'dO;                         
                    .d0o:cdo,.l0kc::;,lOxox0k:.;kOd::::;d0:.;k0c      .cdOO,.;x0dc::,:kO;.:xd;dO;    'xO,                         
                     c0xc;.   ,Oo.    ,kxloOd. .dO,     l0:  ,kkc'.. .;lcxk, .oO,    .dO,  .lkOO;    .lO;                         
                    .ckc.     ;xo:,'..;xc..;kd..ox;    .lxc.  .:ooolcc:',dx:..oxl,'. 'xk,   .:xx:.   .lx:.                        
                     ...       .......,,,'..,xkc'..     ...        ..   ....  ..... .;:;.........     ...                         
                                  .:xkkkkkkd;'lkd;.                             .:,..;oxxxxxxxo'                                  
                                    ,x0000O0k' .cddc,.       ..,'.              ;k0doO0000000o.                                   
                                     .oO00000o....';:;,'''..';lc,'.            .o000OkO0000k:.                                    
                                      .;x00000ko;.          .oOO0O:            .x0OkkkO00Oo'                                      
                                        .o0000O:            .o0000o.           ;OOxkO000kc.                                       
                                         .:k000k:.           c000Kx.          .lOkk0000d'                                         
                                           'dO00Oo.          :O00KO,          'xOO000Oc.                                          
                                            .ck000k;         ;O0000l          ;k0000x,                                            
                                              'dO00Ol.       'k00O0x.        ;x000Ol.                                             
                                               .ck000x,      .o00O0k,      .lO000x;                                               
                                                 ,d000Oc..    .lk00x'     ,x000Ol.                                                
                                                  .cO000kdoc::,,lk0x'..;cdO000x;                                                  
                                                    ,x0000O0OOOkxxkkxxxk0000Ol.                                                   
                                                     .lO0000000000O00000000k;.                                                    
                                                       ;x00000OOO0OOO0000Oo.                                                      
                                                        .lO000OxddxO0000k:.                                                       
                                                         .;k000OkxO0000o'                                                         
                                                           .oO0000000k:.                                                          
                                                            .:k0000Od'                                                            
                                                              'o00Oc.                                                             
                                                               .,;'
""")

while True:
    LOGO()
    print("OUR AIMS:")
    print("* PRIVATISE WORLD PEACE")
    print("* PROVIDE HIGH QUALITY SPACE SYSTEMS")
    print("* BE AT THE FOREFRONT OF THE AVIATION AND SPACE TECH SUMMIT")
    print("* REALISE OUR DREAMS OF SPACE EXPLORATION")
    from pygame import mixer
    mixer.init()
    mixer.music.load('THEME.mp3')
    mixer.music.play()
    USER_DEF=input("ENTER YOUR LEVEL OF AUTHRISATION: (USER/ADMIN/EMPLOYEE) ")
    mixer.music.stop()
    if USER_DEF.upper()=="USER":
        USER()
    elif USER_DEF.upper()=="ADMIN":
        ADMIN()
    elif USER_DEF.upper()=="EMPLOYEE":
        EMPLOYEE()
    else: 
        print("ER101: <INVALID_LEVEL_OF_AUTHORISATION{}>")
        print("REFRESH YOUR PAGE TO CONTINUE!")
        break
