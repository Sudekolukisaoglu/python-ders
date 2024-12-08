rehber={
    "5236":{
        "adi":"Rahime SÜZEN",
        "tel":"5214523652"
    },
"5214":{
    "adi":"Sude AKTÜRK",
    "tel":"5214525687"
    }
}
# print(rehber)
print(rehber["5214"]["adi"],rehber["5214"]["tel"])
rehber["5214"]["adi"] = "Sude AKYOL"
print(rehber["5214"]["adi"],rehber["5214"]["tel"])