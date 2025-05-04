def sort(width, height, length, mass):
    volume = (width*height*length)
    package_type = []
    if volume >= 1_000_000 or max(width, height, length)>=150:
        package_type.append('bulky')
    if mass >= 20:
        package_type.append('heavy')
    
    if not package_type:
        return "STANDARD"
    elif "bulky" in package_type and "heavy" in package_type:
        return "REJECTED"
    else:
        return "SPECIAL"