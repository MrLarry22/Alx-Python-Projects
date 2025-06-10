
from datetime import datetime, timedelta

def display_current_datetime():
    current_date=datetime.now() #Get current date and time
    formatted_date=current_date.strftime("%Y-%m-%d  %H:%M:%S") #Format it 
    print("Current date and time:", formatted_date)
    return current_date 

def calculate_future_date(current_date ):
    try:
        days=int(input("Enter number of days to add:")) #Get user input
        future_date=current_date + timedelta(days=days) #Add days
        print("Future date:", future_date.strftime("%Y - %m -%d")) #Format & Display
    except ValueError:
        print("Invalid input.Please enter an integer.")
        
        
def main():
    current=display_current_datetime()
    calculate_future_date(current)
    
if __name__ == "__main__":
        main()
    