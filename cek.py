import requests

# Fungsi untuk memvalidasi lisensi
def validate_license(license_key):
    # Ganti dengan URL yang sesuai dari Cryptolens.io
    url = "https://app.cryptolens.io/api/key/Activate"

    # Ganti dengan auth token Anda dari Cryptolens.io
    auth_token = "WyI4MTg5NTgzNiIsIlRtTkV0ZDNrZGQ3QTZqRFBPb25GUjNqRGhjQVp2S00vQXg4eWQ2RlMiXQ=="

    # Ganti dengan ID produk dan kode verifikasi produk Anda dari Cryptolens.io
    product_id = 25314
    product_secret = "DWUUK-CSWBF-YPMCT-JGGWN"

    # Kirim permintaan POST untuk memvalidasi lisensi
    response = requests.post(url, json={
        "ProductId": product_id,
        "Key": license_key,
        "Sign": True,
        "ProductSecret": product_secret,
    }, headers={
        "Authorization": f"Bearer {auth_token}"
    })

    # Periksa jika permintaan berhasil
    if response.status_code == 200:
        result = response.json()
        if result["result"] == "ok":
            return True, result["license_key_id"]
        else:
            return False, None
    else:
        return False, None

# Contoh penggunaan
if __name__ == "__main__":
    license_key = input("Masukkan lisensi: ")
    is_valid, license_id = validate_license(license_key)
    if is_valid:
        print("Lisensi valid!")
        print("ID Lisensi:", license_id)
    else:
        print("Lisensi tidak valid.")
