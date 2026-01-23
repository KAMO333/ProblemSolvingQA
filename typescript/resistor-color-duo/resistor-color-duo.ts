export function decodedValue(colors: string[]) {
  const colorIndex = COLORS.indexOf(colors[0])
  const secondColorIndex = COLORS.indexOf(colors[1])


  let joinedColors: string = colorIndex.toString() + secondColorIndex.toString()

  return Number(joinedColors)

}

const COLORS = [
      'black',
      'brown',
      'red',
      'orange',
      'yellow',
      'green',
      'blue',
      'violet',
      'grey',
      'white',
    ]
