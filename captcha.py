import random
import string

def generate_captcha():
  # Generate a random string of letters and digits
  captcha_string = ''.join(random.choices(string.ascii_letters + string.digits, k=6))

  # Return the CAPTCHA string
  return captcha_string

def verify_captcha(captcha_string, user_input):
  # Compare the user's input to the CAPTCHA string
  if captcha_string.lower() == user_input.lower():
    # Return True if the strings match (ignoring case)
    return True
  else:
    # Return False if the strings do not match
    return False

# Generate a CAPTCHA string
captcha = generate_captcha()

# Prompt the user to enter the CAPTCHA
print(f'CAPTCHA: {captcha}')
user_input = input(f'Enter the CAPTCHA: ')

# Verify the user's input
if verify_captcha(captcha, user_input):
  print('CAPTCHA verification successful!')
else:
  print('CAPTCHA verification failed.')
