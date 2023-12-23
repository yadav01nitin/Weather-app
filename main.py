try:

    import requests
    import json
    import pyttsx3
    while True:
        city=input("Enter the name of the city\n")
        if city=="q":
            break

        url=f"https://api.weatherapi.com/v1/current.json?key=0ebcafaa21d64e6091e173737231308&q={city}"

        r=requests.get(url)
        #print(r.text)
        #print(type(r.text))

        wdict=json.loads(r.text)
        w=wdict["current"]["temp_c"]
        print(w)

        engine=pyttsx3.init()
        engine.say(f"The current weather in {city} is {w} degrees")
        engine.runAndWait()


except Exception as e:
    print("some error has eccured",e)
