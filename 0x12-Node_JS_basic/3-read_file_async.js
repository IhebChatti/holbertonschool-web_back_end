const fs = require('fs');

async function countStudents(filepath) {
  try {
    const csv = await fs.promises.readFile(filepath, { encoding: 'utf8' });
    const myList = [];
    const array = csv.split(/\r?\n|\n/);
    const headers = array[0].split(',');
    const noArray = array.slice(1);
    for (let i = 0; i < noArray.length; i += 1) {
      const result = noArray[i].split(',');
      if (result.length === headers.length) {
        const row = {};
        for (let j = 0; j < headers.length; j += 1) {
          row[headers[j].trim()] = result[j].trim();
        }
        myList.push(row);
      }
    }
    let csCount = 0;
    let sweCount = 0;
    const csStudents = [];
    const sweStudents = [];

    myList.forEach((item) => {
      if (item.field === 'CS') {
        csCount += 1;
        csStudents.push(item.firstname);
      } else if (item.field === 'SWE') {
        sweCount += 1;
        sweStudents.push(item.firstname);
      }
    });

    const countStudents = csCount + sweCount;

    console.log(`Number of students: ${countStudents}`);
    console.log(`Number of students in CS: ${csCount}. List: ${csStudents.toString().split(',').join(', ')}`);
    console.log(`Number of students in SWE: ${sweCount}. List: ${sweStudents.toString().split(',').join(', ')}`);
  } catch (err) {
    throw new Error('Cannot load the database');
  }
}

module.exports = countStudents;
