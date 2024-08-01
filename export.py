import os
import urllib.request

# Directory target
TARGET_DIR = r"E:\PSU DATA\EXPORT\KelPisang"

# Mendapatkan layer yang aktif
layer = iface.activeLayer()

# Pastikan layer aktif
if layer is not None:
    # Mendapatkan nama field atribut yang ingin diekstrak
    field_name = "___att"
    
    # Mengecek apakah field tersebut ada di layer
    if field_name in [field.name() for field in layer.fields()]:
        # Iterasi melalui setiap fitur pada layer
        for feature in layer.getFeatures():
            # Mendapatkan nilai dari field atribut
            att_value = feature[field_name]
            
            # Pastikan att_value adalah string
            if isinstance(att_value, str):
                # Memisahkan nilai untuk mendapatkan nama-nama file
                attachments = att_value.split(";")
                
                # Iterasi melalui setiap attachment
                for attachment in attachments:
                    # Memisahkan informasi attachment
                    attachment_info = attachment.split("#")
                    
                    # Pastikan attachment_info memiliki 3 elemen
                    if len(attachment_info) == 3:
                        file_name = attachment_info[0]
                        file_type = attachment_info[1]
                        file_date = attachment_info[2]
                        
                        # Mendapatkan URL file
                        file_url = "https://sirumahkita.padang.go.id/static/attachment/" + file_name
                        
                        # Mendownload file dan menyimpannya di directory target
                        file_path = os.path.join(TARGET_DIR, file_name)
                        urllib.request.urlretrieve(file_url, file_path)
                        
                        # Cetak pesan bahwa file telah didownload
                        print("File", file_name, "telah didownload dan disimpan di", TARGET_DIR)
            else:
                print("Nilai field", field_name, "bukanlah string.")
    else:
        print("Field", field_name, "tidak ditemukan di layer.")
else:
    print("Tidak ada layer yang aktif.")



#-----------------------------------------------------------------------------------------------------
import os
import urllib.request

# Directory target
TARGET_DIR = r"E:\PSU DATA\EXPORT\KelPisang"

# Mendapatkan layer yang aktif
layer = iface.activeLayer()

# Pastikan layer aktif
if layer is not None:
    # Mendapatkan nama field atribut yang ingin diekstrak
    field_name = "___att"
    no_survey_field = "no_survey"  # Nama field untuk no_survey
    
    # Mengecek apakah field-field tersebut ada di layer
    if field_name in [field.name() for field in layer.fields()] and no_survey_field in [field.name() for field in layer.fields()]:
        # Iterasi melalui setiap fitur pada layer
        for feature in layer.getFeatures():
            # Mendapatkan nilai dari field atribut
            att_value = feature[field_name]
            no_survey_value = feature[no_survey_field]
            
            # Pastikan att_value adalah string
            if isinstance(att_value, str):
                # Memisahkan nilai untuk mendapatkan nama-nama file
                attachments = att_value.split(";")
                
                # Iterasi melalui setiap attachment
                for attachment in attachments:
                    # Memisahkan informasi attachment
                    attachment_info = attachment.split("#")
                    
                    # Pastikan attachment_info memiliki 3 elemen
                    if len(attachment_info) == 3:
                        file_name = attachment_info[0]
                        file_type = attachment_info[1]
                        file_date = attachment_info[2]
                        
                        # Mendapatkan URL file
                        file_url = "https://sirumahkita.padang.go.id/static/attachment/" + file_name
                        
                        # Mendownload file dan menyimpannya di directory target dengan nama dari no_survey
                        new_file_name = f"{no_survey_value}_{file_name}"
                        file_path = os.path.join(TARGET_DIR, new_file_name)
                        urllib.request.urlretrieve(file_url, file_path)
                        
                        # Cetak pesan bahwa file telah didownload
                        print(f"File {file_name} telah didownload dan disimpan sebagai {new_file_name} di {TARGET_DIR}")
            else:
                print(f"Nilai field {field_name} bukanlah string.")
    else:
        print(f"Field {field_name} atau {no_survey_field} tidak ditemukan di layer.")
else:
    print("Tidak ada layer yang aktif.")

