# a = open(f"rehber.txt","w")
#  # w=write modunda öncekiler silinir.
a = open(f"rehber.txt","a")
# a=append ile açıldığında öncekilere eklenir.
for b in range (10):
    # a.write(str(b))
    a.write(f"{str(b)}\n")

  