import os

user_config_path = os.path.expanduser('~/.cookiecutterrc')

if not os.path.exists(user_config_path):
  print("""
        PROTIP:

        Make your cookiecutting life easier by creating a ~/.cookiecutterrc file with the following content:
        default_context:
            full_name': "Firstname Lastname",
            email: "firstname.lastname@email.com"

        Use the following command to create the file with the above content:
          make cookiecutterrc
        """)
