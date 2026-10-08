import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# Initialize variables
sales_df = None
current_plot = None


def load_dataset(file_path):
    """Load a CSV dataset safely."""
    global sales_df

    try:
        df = pd.read_csv(file_path)

        if df.empty:
            print("Warning: The dataset is empty.")

        sales_df = df
        print("Dataset loaded successfully!")
        print(f"Rows: {sales_df.shape[0]}")
        print(f"Columns: {sales_df.shape[1]}")

    except FileNotFoundError:
        print("Dataset file not found!")
    except pd.errors.EmptyDataError:
        print("Error: The CSV file is empty.")
    except pd.errors.ParserError:
        print("Error: The CSV file could not be parsed.")
    except PermissionError:
        print("Error: Permission denied.")
    except (OSError, UnicodeError) as error:
        print(f"Error loading dataset: {error}")


def dataset_loaded():
    """Check whether a dataset has been loaded."""
    if sales_df is None:
        print("Please load a dataset first using option 1.")
        return False
    return True


def get_column(prompt):
    """Validate a column name entered by the user."""
    column = input(prompt).strip()

    if column not in sales_df.columns:
        print(f"Invalid column name: {column}")
        print("Available columns:", sales_df.columns.tolist())
        return None

    return column


def create_plot():
    """Create and store a new Matplotlib figure."""
    global current_plot
    current_plot = plt.figure()
    return current_plot


# Attempt to load the default dataset.
load_dataset("data/my_sales_data.csv")


while True:

    print("\n========== Sales Data Analysis Program ==========")
    print("1. Load Dataset")
    print("2. Explore Data")
    print("3. Perform DataFrame Operations")
    print("4. Handle Missing Data")
    print("5. Generate Descriptive Statistics")
    print("6. Data Visualization")
    print("7. Save Visualization")
    print("8. Exit")
    print("=================================================")

    main_choice = input("Enter your choice: ").strip()

    # 1. Load Dataset
    if main_choice == "1":

        print("\n== Load Dataset ==")

        file_path = input(
            "Enter the path of the dataset (CSV file): "
        ).strip()

        load_dataset(file_path)

    # 2. Explore Data
    elif main_choice == "2":

        if not dataset_loaded():
            continue

        while True:
            print("\n== Explore Data ==")
            print("1. Display the first 5 rows")
            print("2. Display the last 5 rows")
            print("3. Display column names")
            print("4. Display data types")
            print("5. Display basic info")
            print("6. Back to the main menu")

            option = input("Enter your choice: ").strip()

            if option == "1":
                print(sales_df.head())

            elif option == "2":
                print(sales_df.tail())

            elif option == "3":
                print(sales_df.columns.tolist())

            elif option == "4":
                print(sales_df.dtypes)

            elif option == "5":
                sales_df.info()

            elif option == "6":
                print("Back to the main menu.")
                break

            else:
                print("Invalid choice. Please enter 1-6.")

    # 3. Perform DataFrame Operations
    elif main_choice == "3":

        if not dataset_loaded():
            continue

        while True:
            print("\n== Perform DataFrame Operations ==")
            print("1. Display Shape")
            print("2. Display Columns")
            print("3. Sort Data")
            print("4. Filter Data")
            print("5. Back to the main menu")

            operation_choice = input(
                "Enter your choice: "
            ).strip()

            if operation_choice == "1":
                print("\nShape:")
                print(sales_df.shape)

            elif operation_choice == "2":
                print("\nColumns:")
                print(sales_df.columns.tolist())

            elif operation_choice == "3":
                column = get_column(
                    "Enter the column to sort by: "
                )

                if column is not None:
                    order = input(
                        "Sort ascending? (y/n): "
                    ).strip().lower()

                    ascending = order != "n"

                    print("\nSorted Data:")
                    print(
                        sales_df.sort_values(
                            by=column,
                            ascending=ascending
                        )
                    )

            elif operation_choice == "4":
                if "Amount" not in sales_df.columns:
                    print("The dataset has no 'Amount' column.")
                    continue

                amount = pd.to_numeric(
                    sales_df["Amount"],
                    errors="coerce"
                )

                print("\nFiltered Data (Amount > 600):")
                print(sales_df.loc[amount > 600])

            elif operation_choice == "5":
                print("Back to the main menu.")
                break

            else:
                print("Invalid choice. Please enter 1-5.")

    # 4. Handle Missing Data
    elif main_choice == "4":

        if not dataset_loaded():
            continue

        while True:
            print("\n== Handle Missing Data ==")
            print("1. Display rows with missing values")
            print("2. Fill missing values with mean")
            print("3. Drop rows with missing values")
            print("4. Replace missing values with a specific value")
            print("5. Back to the main menu")

            missing_option = input(
                "Enter your choice: "
            ).strip()

            if missing_option == "1":

                missing_rows = sales_df[
                    sales_df.isna().any(axis=1)
                ]

                if missing_rows.empty:
                    print("No missing values found!")
                else:
                    print(missing_rows)

            elif missing_option == "2":

                numeric_columns = sales_df.select_dtypes(
                    include="number"
                ).columns

                if len(numeric_columns) == 0:
                    print("No numeric columns available.")
                    continue

                means = sales_df[numeric_columns].mean()

                sales_df[numeric_columns] = (
                    sales_df[numeric_columns].fillna(means)
                )

                print(
                    "Missing numeric values filled with column means."
                )
                print(
                    "Missing values remaining:",
                    sales_df.isna().sum().sum()
                )

            elif missing_option == "3":

                before = len(sales_df)
                sales_df.dropna(inplace=True)
                removed = before - len(sales_df)

                print(f"{removed} rows with missing values dropped.")

            elif missing_option == "4":

                replacement_value = input(
                    "Enter replacement value: "
                ).strip()

                # Interpret numeric input as a number.
                try:
                    replacement_value = float(replacement_value)
                except ValueError:
                    pass

                sales_df.fillna(
                    replacement_value,
                    inplace=True
                )

                print("Missing values replaced successfully.")
                print(
                    "Missing values remaining:",
                    sales_df.isna().sum().sum()
                )

            elif missing_option == "5":
                print("Back to the main menu.")
                break

            else:
                print("Invalid choice. Please enter 1-5.")

    # 5. Generate Descriptive Statistics
    elif main_choice == "5":

        if not dataset_loaded():
            continue

        print("\n== Descriptive Statistics ==")
        print(sales_df.describe(include="all"))

    # 6. Data Visualization
    elif main_choice == "6":

        if not dataset_loaded():
            continue

        while True:
            print("\n== Data Visualization ==")
            print("1. Bar Plot")
            print("2. Line Plot")
            print("3. Scatter Plot")
            print("4. Pie Chart")
            print("5. Histogram")
            print("6. Stack Plot")
            print("7. Back to the main menu")

            chart_choice = input(
                "Enter your choice: "
            ).strip()

            try:

                if chart_choice == "1":

                    x_column = get_column(
                        "Enter x-axis column name: "
                    )
                    if x_column is None:
                        continue

                    y_column = get_column(
                        "Enter y-axis column name: "
                    )
                    if y_column is None:
                        continue

                    fig = create_plot()

                    plt.bar(
                        sales_df[x_column],
                        sales_df[y_column]
                    )
                    plt.xlabel(x_column)
                    plt.ylabel(y_column)
                    plt.title("Sales Bar Plot")
                    plt.xticks(rotation=45)
                    plt.tight_layout()

                    print("Generating bar plot...")
                    plt.show()

                elif chart_choice == "2":

                    x_column = get_column(
                        "Enter x-axis column name: "
                    )
                    if x_column is None:
                        continue

                    y_column = get_column(
                        "Enter y-axis column name: "
                    )
                    if y_column is None:
                        continue

                    fig = create_plot()

                    plt.plot(
                        sales_df[x_column],
                        sales_df[y_column],
                        marker="o"
                    )
                    plt.xlabel(x_column)
                    plt.ylabel(y_column)
                    plt.title("Sales Line Plot")
                    plt.xticks(rotation=45)
                    plt.tight_layout()

                    print("Generating line plot...")
                    plt.show()

                elif chart_choice == "3":

                    x_column = get_column(
                        "Enter x-axis column name: "
                    )
                    if x_column is None:
                        continue

                    y_column = get_column(
                        "Enter y-axis column name: "
                    )
                    if y_column is None:
                        continue

                    x_values = pd.to_numeric(
                        sales_df[x_column],
                        errors="coerce"
                    )
                    y_values = pd.to_numeric(
                        sales_df[y_column],
                        errors="coerce"
                    )

                    valid = x_values.notna() & y_values.notna()

                    if not valid.any():
                        print("No valid numeric data to plot.")
                        continue

                    fig = create_plot()

                    plt.scatter(
                        x_values[valid],
                        y_values[valid]
                    )
                    plt.xlabel(x_column)
                    plt.ylabel(y_column)
                    plt.title("Sales Scatter Plot")
                    plt.tight_layout()

                    print("Generating scatter plot...")
                    plt.show()

                elif chart_choice == "4":

                    category_column = get_column(
                        "Enter category column name: "
                    )
                    if category_column is None:
                        continue

                    category_values = sales_df[
                        category_column
                    ].dropna().value_counts()

                    if category_values.empty:
                        print("No category data available.")
                        continue

                    fig = create_plot()

                    plt.pie(
                        category_values,
                        labels=category_values.index,
                        autopct="%1.1f%%"
                    )
                    plt.title("Sales Pie Chart")
                    plt.tight_layout()

                    print("Generating pie chart...")
                    plt.show()

                elif chart_choice == "5":

                    selected_column = get_column(
                        "Enter column name: "
                    )
                    if selected_column is None:
                        continue

                    values = pd.to_numeric(
                        sales_df[selected_column],
                        errors="coerce"
                    ).dropna()

                    if values.empty:
                        print("No numeric data available.")
                        continue

                    fig = create_plot()

                    plt.hist(values, bins=10)
                    plt.xlabel(selected_column)
                    plt.ylabel("Frequency")
                    plt.title("Sales Histogram")
                    plt.tight_layout()

                    print("Generating histogram...")
                    plt.show()

                elif chart_choice == "6":

                    numeric_data = sales_df.select_dtypes(
                        include="number"
                    )

                    if numeric_data.shape[1] == 0:
                        print("No numeric columns available.")
                        continue

                    # Use up to three numeric columns.
                    stack_data = numeric_data.iloc[:, :3].copy()

                    # Remove columns that contain no usable values.
                    stack_data = stack_data.dropna(axis=1, how="all")

                    if stack_data.empty:
                        print("No numeric data available.")
                        continue

                    # Fill remaining missing values for plotting.
                    stack_data = stack_data.fillna(0)

                    fig = create_plot()

                    plt.stackplot(
                        range(len(stack_data)),
                        *[
                            stack_data[col].to_numpy()
                            for col in stack_data.columns
                        ],
                        labels=stack_data.columns
                    )

                    plt.xlabel("Index")
                    plt.ylabel("Values")
                    plt.title("Sales Stack Plot")
                    plt.legend()
                    plt.tight_layout()

                    print("Generating stack plot...")
                    plt.show()

                elif chart_choice == "7":
                    print("Back to the main menu.")
                    break

                else:
                    print("Invalid choice. Please enter 1-7.")

            except (KeyError, ValueError, TypeError) as error:
                print(f"Unable to generate plot: {error}")

    # 7. Save Visualization
    elif main_choice == "7":

        print("\n== Save Visualization ==")

        if current_plot is None:
            print("No visualization available!")
            continue

        save_name = input(
            "Enter file name (e.g., sales_plot.png): "
        ).strip()

        if not save_name:
            print("File name cannot be empty.")
            continue

        try:
            save_path = Path(save_name)

            if save_path.suffix.lower() not in (
                ".png", ".jpg", ".jpeg", ".pdf", ".svg"
            ):
                print(
                    "Unsupported format. Use PNG, JPG, JPEG, PDF, or SVG."
                )
                continue

            current_plot.savefig(
                save_path,
                bbox_inches="tight"
            )

            print(f"Visualization saved successfully: {save_path}")

        except (OSError, ValueError) as error:
            print(f"Unable to save visualization: {error}")

    # 8. Exit
    elif main_choice == "8":

        print("\nExiting the program. Goodbye!")
        plt.close("all")
        break

    else:
        print("Invalid choice! Please enter a number from 1 to 8.")