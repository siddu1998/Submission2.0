directions=["NE", "E", "SE", "S", "SW", "W", "NW", "N"]

index = brng - 22.5

if index < 0
    index += 360
index = parseInt(index / 45)

return(bearings[index])