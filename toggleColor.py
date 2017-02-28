def toggleColor(r, g, b, increment, colorMax):
  if r > 10 && r < colorMax:
    if g == colorMax:
      r -= increment
      if r <= 10:
        r = 10
        b = 10 + increment
    else:
      r += increment
      if r >= colorMax:
        r = colorMax
        b = colorMax - increment
  else if g > 10 && g < colorMax:
    if b == colorMax:
      g -= increment
      if g <= 10:
        g = 10
        r = 10 + increment
    else:
      g += increment
      if g >= colorMax:
        g = colorMax
        r = colorMax - increment
  else:
    if r == colorMax:
      b -= increment
      if b <= 10:
        b = 10
        g = 10 + increment
    else:
      b += increment
      if b >= colorMax:
        b = colorMax
        g = colorMax - increment
  return [r, g, b]
