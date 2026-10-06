import pandas as pd
import matplotlib.pyplot as plt


sales_df = pd.DataFrame(sales_data)
current_plot = None

while True:

    print("\n========== Sales Data Analysis Program ==========")
    print("Please select an option:")
    print("1. Load Dataset")
    print("2. Explore Data")
    print("3. Perform DataFrame Operations")
    print("4. Handle Missing Data")
    print("5. Generate Descriptive Statistics")
    print("6. Data Visualization")
    print("7. Save Visualization")
    print("8. Exit")
    print("=================================================")

    main_choice = input("\nEnter your choice: ")


    if main_choice == "1":

        print("\n== Load Dataset ==")

        file_path = input(
            "Enter the path of the dataset (CSV file): "
        )

        try:
            sales_df = pd.read_csv(file_path)
            print("Dataset loaded successfully!")

        except FileNotFoundError:
            print("Dataset file not found!")


    elif main_choice == "2":
      
      while True:
        print("\n== Explore Data ==")
        print("1. Display the first 5 rows")
        print("2. Display the last 5 rows")
        print("3. Display column names")
        print("4. Display data types")
        print("5. Display basic info")
        print("6. Back to the main menu")
        print("=================================================")

        option = input("Enter your choice: ")

        if option == "1":

            print()
            print(sales_df.head())

        elif option == "2":

            print()
            print(sales_df.tail())

        elif option == "3":

            print()
            print(sales_df.columns)

        elif option == "4":

            print()
            print(sales_df.dtypes)

        elif option == "5":

            print()
            sales_df.info()
        elif option == "6":
            print("Back to the main menu")
            break
        else:
            print("Invalid index")


    elif main_choice == "3":
      while True:
        print("\n== Perform DataFrame Operations ==")
        print("1. Display Shape")
        print("2. Display Columns")
        print("3. Sort Data")
        print("4. Filter Data")
        print("5. Back to the main menu")
        print("=================================================") 

        operation_choice = input("Enter your choice: ")

        if operation_choice == "1":

            print("\nShape:")
            print(sales_df.shape)

        elif operation_choice == "2":

            print("\nColumns:")
            print(sales_df.columns.tolist())

        elif operation_choice == "3":

            print("\nSorted Data:")
            print(sales_df.sort_values("Amount"))

        elif operation_choice == "4":

            print("\nFiltered Data:")
            print(sales_df[sales_df["Amount"] > 600])

        elif operation_choice == "5":
            print("Back to the main menu")
            break
        else:
            print("Invalid index")
        

    elif main_choice == "4":
      while True:

        print("\n== Handle Missing Data ==")
        print("1. Display rows with missing values")
        print("2. Fill missing values with mean")
        print("3. Drop rows with missing values")
        print("4. Replace missing values with a specific value")
        print("5. Back to the main menu")
        print("=================================================")
        missing_option = input("Enter your choice: ")

        if missing_option == "1":

            if sales_df.isnull().sum().sum() == 0:

                print("\nNo missing values found in the dataset!")

            else:

                print(
                    sales_df[sales_df.isnull().any(axis=1)]
                )

        elif missing_option == "2":

            sales_df.fillna(
                sales_df.mean(numeric_only=True),
                inplace=True
            )

            print("Missing values filled successfully!")

        elif missing_option == "3":

            sales_df.dropna(inplace=True)

            print("Rows with missing values dropped!")

        elif missing_option == "4":

            replacement_value = input("Enter value: ")

            sales_df.fillna(
                replacement_value,
                inplace=True
            )

            print("Missing values replaced successfully!")

        elif missing_option == "5":
            print("Back to the main menu")
            break
        else:
            print("Invalid index")


    elif main_choice == "5":

        print("\n== Descriptive Statistics ==")

        print(sales_df.describe())


    elif main_choice == "6":
      while True:

        print("\n== Data Visualization ==")
        print("1. Bar Plot")
        print("2. Line Plot")
        print("3. Scatter Plot")
        print("4. Pie Chart")
        print("5. Histogram")
        print("6. Stack Plot")
        print("7. Back to the main menu")

        chart_choice = input("Enter your choice: ")


        if chart_choice == "1":

            x_column = input("Enter x-axis column name: ")
            y_column = input("Enter y-axis column name:")

            plt.figure()

            plt.bar(
                sales_df[x_column],
                sales_df[y_column]
            )

            plt.xlabel(x_column)
            plt.ylabel(y_column)
            plt.title("Sales Bar Plot")

            current_plot = plt.gcf()

            print("Generating bar plot...")

            plt.show()

            print("Bar plot displayed successfully!")


        elif chart_choice == "2":

            x_column = input("Enter x-axis column name: ")
            y_column = input("Enter y-axis column name: ")

            plt.figure()

            plt.plot(
                sales_df[x_column],
                sales_df[y_column],
                marker="o"
            )

            plt.xlabel(x_column)
            plt.ylabel(y_column)
            plt.title("Sales Line Plot")

            current_plot = plt.gcf()

            print("Generating line plot...")

            plt.show()

            print("Line plot displayed successfully!")


        elif chart_choice == "3":

            print("\n== Scatter Plot ==")

            x_column = input("Enter x-axis column name: ")
            y_column = input("Enter y-axis column name: ")

            plt.figure()

            plt.scatter(
                sales_df[x_column],
                sales_df[y_column]
            )

            plt.xlabel(x_column)
            plt.ylabel(y_column)
            plt.title("Sales Scatter Plot")

            current_plot = plt.gcf()

            print("Generating scatter plot...")

            plt.show()

            print("Scatter plot displayed successfully!")


        elif chart_choice == "4":

            category_column = input("Enter column name: ")

            category_values = sales_df[
                category_column
            ].value_counts()

            plt.figure()

            plt.pie(
                category_values,
                labels=category_values.index,
                autopct="%1.1f%%"
            )

            plt.title("Sales Pie Chart")

            current_plot = plt.gcf()

            print("Generating pie chart...")

            plt.show()

            print("Pie chart displayed successfully!")


        elif chart_choice == "5":

            selected_column = input("Enter column name: ")

            plt.figure()

            plt.hist(
                sales_df[selected_column],
                bins=10
            )

            plt.xlabel(selected_column)
            plt.ylabel("Frequency")
            plt.title("Sales Histogram")

            current_plot = plt.gcf()

            print("Generating histogram...")

            plt.show()

            print("Histogram displayed successfully!")


        elif chart_choice == "6":

            numeric_data = sales_df.select_dtypes(
                include="number"
            )

            plt.figure()

            plt.stackplot(
                range(len(sales_df)),
                *numeric_data.iloc[:, :3].T.values,
                labels=numeric_data.columns[:3]
            )

            plt.xlabel("Index")
            plt.ylabel("Values")
            plt.title("Sales Stack Plot")

            plt.legend()

            current_plot = plt.gcf()

            print("Generating stack plot...")

            plt.show()

            print("Stack plot displayed successfully!")

        elif chart_choice == "5":
            print("Back to the main menu")
            break
        else:
            print("Invalid index")
        
        


    elif main_choice == "7":

        print("\n== Save Visualization ==")

        save_name = input(
            "Enter file name to save the plot "
            "(e.g., sales_plot.png): "
        )

        if current_plot is not None:

            current_plot.savefig(save_name)

            print(
                "Visualization saved as "
                + save_name
                + " successfully!"
            )

        else:

            print("No visualization available!")


    elif main_choice == "8":

        print("\nExiting the program. Goodbye!")

        break


    else:

        print("\nInvalid choice! Please try again.")
