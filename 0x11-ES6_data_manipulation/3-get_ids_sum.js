export default function getStudentIdsSum(students) {
  if (Object.getPrototypeOf(students) === Array.prototype) {
    const studentsIds = students.map((student) => student.id);
    const reducer = (accumlator, value) => accumlator + value;
    return studentsIds.reduce(reducer);
  }
  return [];
}
