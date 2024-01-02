a=int(input("Enter your age: "))
b=str(input("Enter your employment status (employed/unemployed): "))
c=str(input("Enter your Martial status (married/unmarried): "))
if a<25:
    print ("Not Allowed for insurance ")
if a>=25 and a<=40 and b=='unemployed'and c=='unmarried':
    print('insurance plan is 1400Pkr/month')
if a>=25 and a<=40 and b=='employed'and c=='unmarried':
    print('insurance plan is 800Pkr/month')
if a>=25 and a<=40 and b=='unemployed'and c=='married':
    print('insurance plan is 1200Pkr/month')
if a>=25 and a<=40 and b=='employed' and c=='married':
    print('insurance plan is 1000Pkr/month')
if a>40:
    print('insurance plan is 1500Pkr/month')