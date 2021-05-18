export default function getStudentsByLocation(students, city) {
  if (Object.getPrototypeOf(students) === Array.prototype) {
    return students.filter((student) => student.location === city);
  }
  return [];
}
