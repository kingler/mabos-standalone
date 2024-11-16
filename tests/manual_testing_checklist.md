# Manual Testing Checklist for MABOS

## Setup
- [ ] Backend server is running with HTTPS (`uvicorn src.api.main:app --reload --ssl-keyfile=localhost.key --ssl-certfile=localhost.crt`)
- [ ] Frontend development server is running with HTTPS (`npm run start:https` in the frontend directory)
- [ ] ArangoDB is running and accessible
- [ ] Redis server is running for rate limiting

## Security Measures
### HTTPS
- [ ] All communication between frontend and backend is over HTTPS
- [ ] Browser shows secure connection icon

### CSRF Protection
- [ ] CSRF token is included in all POST, PUT, and DELETE requests
- [ ] Requests without proper CSRF token are rejected

### Rate Limiting
- [ ] Login attempts are rate-limited (5 attempts per minute)
- [ ] Registration attempts are rate-limited (3 attempts per minute)
- [ ] Exceeding rate limits results in appropriate error messages

### Secure Headers
- [ ] X-XSS-Protection header is present and set to "1; mode=block"
- [ ] X-Frame-Options header is present and set to "DENY"
- [ ] X-Content-Type-Options header is present and set to "nosniff"
- [ ] Strict-Transport-Security header is present and set appropriately
- [ ] Content-Security-Policy header is present and set correctly

### Content Security Policy (CSP)
- [ ] Verify that the CSP meta tag is present in the index.html file
- [ ] No inline scripts are present in the HTML
- [ ] No inline styles are present in the HTML
- [ ] External resources (if any) are properly whitelisted in the CSP
- [ ] Console shows no CSP violation errors during normal operation of the application

### Secure Password Storage
- [ ] Passwords are not stored in plain text (check database entries)
- [ ] Password hashing uses bcrypt

### Automated Security Scanning
- [ ] GitHub Actions workflow for security scanning is present (.github/workflows/security-scan.yml)
- [ ] Security scan runs automatically on pull requests to the main branch
- [ ] Nightly security scans are scheduled and running
- [ ] Security scan reports are generated and uploaded as artifacts
- [ ] High and medium severity issues trigger a workflow failure
- [ ] Slack notifications are sent with scan results (if configured)

## Authentication and Authorization
### User Registration
- [ ] Registration form is accessible from the login page
- [ ] Registration form includes fields for username, email, and password
- [ ] Submitting the form with valid data creates a new user account
- [ ] Submitting the form with an existing username shows an error message
- [ ] Password confirmation is required and validated
- [ ] Email format is validated
- [ ] After successful registration, a success message is displayed informing the user to check their email
- [ ] A verification email is sent to the user's email address

### Email Verification
- [ ] Verification email is received after registration
- [ ] Verification email contains a valid verification link
- [ ] Clicking the verification link in the email redirects to the verification page
- [ ] Successful verification displays a success message
- [ ] After successful verification, the user can log in
- [ ] Attempting to log in before verification shows an "Email not verified" error message
- [ ] Attempting to use an invalid or expired verification link shows an error message

### Two-Factor Authentication (2FA)
- [ ] Users can access the 2FA setup page
- [ ] Users can enable 2FA for their account
- [ ] QR code is displayed when enabling 2FA
- [ ] Users can disable 2FA for their account
- [ ] Login process requires 2FA token when 2FA is enabled
- [ ] Invalid 2FA token results in login failure
- [ ] Valid 2FA token allows successful login
- [ ] Users can log in successfully after disabling 2FA

### User Login
- [ ] Login form is displayed when not authenticated
- [ ] Login form includes fields for username and password
- [ ] Submitting the form with valid credentials logs the user in
- [ ] Submitting the form with invalid credentials shows an error message
- [ ] Attempting to log in with an unverified email shows an appropriate error message
- [ ] Successful login redirects to the main application interface
- [ ] User session persists after page reload

### User Logout
- [ ] Logout button is visible when user is logged in
- [ ] Clicking logout button logs the user out
- [ ] After logout, user is redirected to the login page
- [ ] Logged out user cannot access protected routes without logging in again

### Role-based Access Control
- [ ] Admin users can access all features (create, read, update, delete goals, view efficiency analysis)
- [ ] Manager users can create, read, and update goals, and view efficiency analysis
- [ ] Regular users can only read goals and get recommendations
- [ ] User's role is displayed in the header after login
- [ ] Attempting to access unauthorized features shows appropriate error messages

## Health Check
- [ ] Application loads without errors
- [ ] Health status is displayed correctly in the frontend
- [ ] Database connection status is accurate

## Goal Management
### Creating a Goal (Admin and Manager only)
- [ ] Goal creation form is displayed with all required fields
- [ ] Date picker is working for start and end dates
- [ ] Form validation prevents submission with empty fields
- [ ] Error messages are displayed for invalid inputs
- [ ] Current value cannot exceed target value
- [ ] End date must be after start date
- [ ] Form submission creates a new goal
- [ ] Newly created goal appears in the goal list
- [ ] Success notification is displayed after goal creation
- [ ] Form is cleared after successful submission

### Listing Goals (All users)
- [ ] All created goals are displayed in the goal list
- [ ] Goal details (name, description, target value, current value, status) are correctly shown
- [ ] Progress bar accurately represents goal progress
- [ ] "No goals found" message is displayed when the list is empty

### Updating Goal Progress (Admin and Manager only)
- [ ] Edit button is present for each goal (only for Admin and Manager)
- [ ] Clicking edit opens the goal form with pre-filled data
- [ ] Changes can be made to all fields
- [ ] Updating current value changes the goal's status if applicable
- [ ] Changes are reflected immediately in the UI after saving
- [ ] Success notification is displayed after updating progress

### Deleting a Goal (Admin only)
- [ ] Delete button is present for each goal (only for Admin)
- [ ] Clicking delete shows a confirmation dialog
- [ ] Confirming deletion removes the goal from the list
- [ ] Cancelling deletion keeps the goal in the list
- [ ] Deleted goal does not reappear after refreshing
- [ ] Success notification is displayed after deleting a goal

### Goal Recommendations (All users)
- [ ] "Get Recommendations" button is present for each goal
- [ ] Clicking the button fetches and displays recommendations
- [ ] Recommendations are relevant to the goal's progress

## Efficiency Analysis (Admin and Manager only)
- [ ] Efficiency Analysis section is visible on the main page (only for Admin and Manager)
- [ ] Average Efficiency Score is displayed and appears to be calculated correctly
- [ ] Total Goals count matches the number of goals in the list
- [ ] Completed Goals, In Progress Goals, and Overdue Goals counts are displayed
- [ ] Recommendations for improving efficiency are shown
- [ ] "Refresh Analysis" button is present and functional
- [ ] Efficiency Analysis updates when goals are added, updated, or deleted

## Error Handling
- [ ] Attempting to create a goal with missing fields shows appropriate error messages
- [ ] Attempting to set end date before start date shows an error message
- [ ] Attempting to set current value higher than target value shows an error message
- [ ] Attempting to access unauthorized features shows appropriate error messages
- [ ] Network errors (e.g., if the backend is down) are handled gracefully with error notifications
- [ ] Error messages are clear and informative

## UI/UX
- [ ] Layout is responsive and adapts well to different screen sizes
- [ ] Goal management and Efficiency Analysis sections are clearly separated
- [ ] Buttons and inputs are properly styled and easy to interact with
- [ ] Date picker is easy to use and visually appealing
- [ ] Progress bars clearly show goal progress
- [ ] Notifications (success and error) are displayed prominently and disappear after a few seconds
- [ ] Loading states are displayed when appropriate (e.g., during form submission, goal deletion, fetching efficiency analysis)
- [ ] Color scheme is consistent and visually appealing
- [ ] Edit and delete confirmation modals are displayed correctly and easy to interact with
- [ ] Login and registration forms are visually appealing and easy to use
- [ ] Switching between login and registration forms is intuitive
- [ ] Logout button is clearly visible and accessible
- [ ] User role is clearly displayed in the header
- [ ] 2FA setup page is easy to navigate and use

## Performance
- [ ] Application remains responsive when dealing with multiple goals
- [ ] Goal list loads quickly, even with many goals
- [ ] Actions (create, update, delete) are performed without noticeable delay
- [ ] Efficiency Analysis loads and updates quickly
- [ ] Login, registration, and logout actions are performed quickly
- [ ] Email verification process completes in a reasonable time
- [ ] 2FA setup and verification process is quick and responsive

## Browser Compatibility
Test the application in different browsers:
- [ ] Chrome
- [ ] Firefox
- [ ] Safari
- [ ] Edge (if available)

## Accessibility
- [ ] All interactive elements are keyboard accessible
- [ ] Form inputs have proper labels
- [ ] Color contrast is sufficient for text readability
- [ ] Error messages are associated with their respective form fields
- [ ] ARIA attributes are used where appropriate

## Integration
- [ ] Changes made in the frontend are correctly reflected in the backend (verify using API documentation at `https://localhost:8000/docs`)
- [ ] Data consistency is maintained across frontend and backend
- [ ] Efficiency Analysis data is consistent with the current state of goals
- [ ] User authentication state is consistent between frontend and backend
- [ ] Role-based permissions are enforced consistently across frontend and backend
- [ ] Email verification process is properly integrated between frontend and backend
- [ ] 2FA setup and verification process is properly integrated between frontend and backend

## Notes
- Add any additional observations, bugs, or improvement suggestions here.

Remember to test on different devices (desktop, tablet, mobile) to ensure responsive design is working correctly.