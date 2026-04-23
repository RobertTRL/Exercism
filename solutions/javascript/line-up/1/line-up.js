//
// This is only a SKELETON file for the 'Line Up' exercise. It's been provided as a
// convenience to get you started writing code faster.
//

export const format = (name, number) => {
  const stringified = number.toString()
  let ordinal
  if (stringified.at(-1) === '1' && !stringified.includes('11')) {
    ordinal = 'st'
  }else if (stringified.at(-1) === '2' && !stringified.includes('12')) {
    ordinal = 'nd'
  }else if (stringified.at(-1) === '3' && !stringified.includes('13')) {
    ordinal = 'rd'
  }else {ordinal = 'th'}
  return `${name}, you are the ${number}${ordinal} customer we serve today. Thank you!`
};
