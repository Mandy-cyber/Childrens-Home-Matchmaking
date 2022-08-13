import sqlite3

# -----------------------------------------------------------------------------------------------------------------#
# SETTING UP DATABASE STUFF
# Connection and cursor
conn = sqlite3.connect('match.db')
cursor = conn.cursor()
matched_home = []
selected_budget_list = []

# -----------------------------------------------------------------------------------------------------------------#
#GETTING THE NECESSARY COLUMNS FROM THE MATCHMAKER TABLES
cursor.execute("SELECT parish FROM matchmaker")
parish_matchmaker = cursor.fetchall()
parish_matchmaker = str(parish_matchmaker).replace('(','').replace(')','').replace('\"','')

cursor.execute("SELECT budget FROM matchmaker")
budget_matchmaker = cursor.fetchall()
budget_matchmaker = str(budget_matchmaker).replace('(','').replace(')','').replace('\"','')
budget_matchmaker = int(budget_matchmaker)
max_budget_matchmaker = budget_matchmaker + 10000
min_budget_matchmaker = budget_matchmaker - 10000

cursor.execute("SELECT type FROM matchmaker")
type_matchmaker = cursor.fetchall()
type_matchmaker = str(type_matchmaker).replace('(','').replace(')','').replace('\"','')

# -----------------------------------------------------------------------------------------------------------------#
# CLEARING THE DATABASE SO THERE WILL ONLY BE ONE ROW OF DATA WHEN THE PROGRAM IS RAN AGAIN
try:
    cursor.execute(f"DELETE FROM matchmaker WHERE id = {1};")

except:
    pass

# -----------------------------------------------------------------------------------------------------------------#
# GETTING THE ROWS FROM THE HOME TABLE THAT HAVE THE SAME PARISH AND HOME TYPE AS SELECTED BY THE USER       
cursor.execute('''SELECT id FROM homes WHERE parish = ? AND type = ?''', (parish_matchmaker, type_matchmaker))
selected_home = cursor.fetchall()

# -----------------------------------------------------------------------------------------------------------------#
# GETTING THE ROWS FROM THE HOME TABLE THAT HAVE THE SAME PARISH AND HOME TYPE AS SELECTED BY THE USER  
for x in selected_home:
    cursor.execute('''SELECT budget FROM homes WHERE id = ?''', (x))
    selected_budgets = cursor.fetchall   
    selected_budget_list.append(selected_budgets)
conn.commit()

for budget in selected_budget_list:
    budget = str(budget_matchmaker).replace('(','').replace(')','').replace('\"','')
    budget = int(budget)

# -----------------------------------------------------------------------------------------------------------------#
# SELECTS THE BUDGETS THAT ARE EITHER $10,000 MORE OR LESS THAN THE BUDGET GIVEN BY THE USER AND THEN FINDS THE ID OF THE BUDGETS 
    if budget in range(min_budget_matchmaker, max_budget_matchmaker):
        budget_index = selected_budget_list.index(budget)
        matched_budget_number = budget_index + 1
        matched_home.append(matched_budget_number)
        
# -----------------------------------------------------------------------------------------------------------------#
# ID IS USED TO FIND THE NAME OF THE MATCHED HOMES 
        for x in matched_home:
            cursor.execute('''SELECT name FROM homes WHERE id = ?''', (x))
            name_of_matched_homes = cursor.fetchall
        conn.commit()
    
    else:
        pass