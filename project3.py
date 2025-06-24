import re

input_file = "sample.txt"
output_file = "extracted_emails.txt"

try:
    with open(input_file, 'r', encoding='utf-8') as file:
        content = file.read()

    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    emails = re.findall(email_pattern, content)

    with open(output_file, 'w', encoding='utf-8') as file:
        for email in emails:
            file.write(email + '\n')

    print(f"✅ Extracted {len(emails)} email(s) and saved to '{output_file}'")

except FileNotFoundError:
    print(f"❌ Error: '{input_file}' was not found.")
except Exception as e:
    print(f"⚠️ An unexpected error occurred: {e}")
