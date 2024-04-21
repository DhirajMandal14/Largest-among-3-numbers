import streamlit as st

def find_largest_number(num1, num2, num3):
    return max(num1, num2, num3)

def main():
    st.title("Largest Number Finder")

    # Sidebar for user input
    st.sidebar.header("Enter 3 Numbers:")
    num1 = st.sidebar.number_input("Number 1", value=0)
    num2 = st.sidebar.number_input("Number 2", value=0)
    num3 = st.sidebar.number_input("Number 3", value=0)

    # Find the largest number
    largest_num = find_largest_number(num1, num2, num3)

    # Display result
    st.write("The largest number is:", largest_num)

if __name__ == "__main__":
    main()
