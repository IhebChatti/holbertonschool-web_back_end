export default function updateUniqueItems(groceries) {
  if (Object.getPrototypeOf(groceries) !== Map.prototype) throw TypeError('Cannot process');

  groceries.forEach((key, value) => {
    if (key === 1) {
      groceries.set(value, 100);
    }
  });
  return groceries;
}
