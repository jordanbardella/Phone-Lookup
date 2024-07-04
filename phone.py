import requests
import sys

def search_phone_number(phone_number):
    api_key = "UYXXd2qpcpWJ1127vT2qo7ZcILbaNnTJ"
    url = f"https://api.apilayer.com/number_verification/validate?number={phone_number}"
    headers = {"apikey": api_key}
    
    try:
        response = requests.get(url, headers=headers)
        data = response.json()
        
        if response.status_code == 200 and data['valid']:
            result = f"-----------------------------------------\n" \
                     f"Numéro de téléphone: {data['number']}\n" \
                     f"Format local: {data['local_format']}\n" \
                     f"Format international: {data['international_format']}\n" \
                     f"Préfixe pays: {data['country_prefix']}\n" \
                     f"Code pays: {data['country_code']}\n" \
                     f"Nom pays: {data['country_name']}\n" \
                     f"Opérateur: {data['carrier']}\n" \
                     f"Type de ligne: {data['line_type']}\n" \
                     f"-----------------------------------------\n"  
            return result
        else:
            return "Numéro de téléphone invalide ou non trouvé."
    except Exception as e:
        return f"Une erreur s'est produite : {str(e)}"

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: phone.py -scan <phone_number>")
        sys.exit(1)

    if sys.argv[1] != "-scan":
        print("Usage: phone.py -scan <phone_number>")
        sys.exit(1)

    phone_number = sys.argv[2]
    result = search_phone_number(phone_number)
    print(result)
