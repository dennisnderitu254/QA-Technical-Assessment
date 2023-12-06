# Quality Assurance Engineer Technical Assessment

# Task 1

Objective: Develop a Comprehensive set of test cases for the `Sign Up` feature, encompassing a varriety of scenarios

## `Instructions`

- Create detailed test cases for the  `Sign Up` feature, categorizing them into positive and negative scenarios.

- `NOTE`:: Ensure Clear Organization in your documentation

### `Test Cases for the Sign Up Feature`

#### Functional Test Cases

1. Verify the prescence of required fields: Ensure all mandatory fields, such as Username, email, password are there, confirm password, as seen in the registration form.

2. Validate Successful registration with valid data: Check if the user can successfully register with valid credentials, and is redirected to a confirmation of login page

3. Handle Invalid usernames: The system should ensure th e prevention of registration of invalid usernames, those containing special characters, symbols, or exidting usernames

4. Validate email format: Ensure the system accepts valid email formatsand displays an error message for invalid or empty email addresses

5. Enforce password strength requirements: Implementation of password complexity rules - like minimum length, character variations, case sensitivity, and also display of appropriate error messages.

6. Validate password confirmation:

7. Handle duplicate user registration attempts:

8. Clear form Data upon successful registration:

#### User Interface Test Cases

1. Check for Clear Labels on fields

2. Verify proper field Formating

3. Test Error Message visibility and clarity

4. Evaluate form layout and responsiveness

5. Test input validation feedback mechanisms

#### Accessibility Test Cases 

1. Verify Keyboard accessibility:

2. Test Color Contrast ans Readability:

3. Check is the reader is able to see the input fields and text

4. Form navigation: The user should be able to move from one field to the next with ease, for good user experience.

#### `Positive and Negative Scenarios in the user Sign Up Test Case`

#### `Positive Scenarios`

1. The user is able to access the keyboard an input fields

2. The error messages are visible and clear for the user, this is seen when the input field of a required field
   is highlighted through an error message.

#### `Negative Scenarios`

1. The user is not able to input fields properly in the form, and no message is sent to alert of correct.

2. The user interface not throwing an error showing duplicate registration, or a username taken.

### `Task 2: Exploratory Testing and Bug Reporting` 

- Identify and Document any bugs of Glitches.

- For Each Issue, Provide a title, a brief description, steps to reproduce, expected vs actual results and severuty assessment