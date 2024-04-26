import os
import face_recognition

print("inserisci la foto del soggetto noto nella cartella \"soggetto\" e le foto da cercare nella cartella \"foto\"")
vai = input("fatto? s/n: ")

if vai == "s":
    for filename in os.listdir("soggetto"):
        soggetto = face_recognition.load_image_file("soggetto/"+filename)
        soggetto_encodings = face_recognition.face_encodings(soggetto)[0]

        for filename_foto in os.listdir("foto"):
            foto = face_recognition.load_image_file("foto/"+filename_foto)
            foto_encoding = face_recognition.face_encodings(foto)[0]

            comparazione = face_recognition.compare_faces([soggetto_encodings], foto_encoding)

            if comparazione[0] == True:
                print("trovato il soggetto nella foto:",filename_foto)
            else:
                print("soggetto non trovato nella foto:",filename_foto)
                
            