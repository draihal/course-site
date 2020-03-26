import React from 'react'
import renderer from 'react-test-renderer'
import { render } from '@testing-library/react'
import TestStudentsHomework from './StudentsHomework'

const homework = [
  {
    "id": 1,
    "grade": {
      "id": 1,
      "teacher_last_name": "Test teacher_last_name 1",
      "status": "rework",
      "grade": "test grade 1",
    },
    "student_first_name": "Student 1",
    "student_last_name": "",
    "student_homework": "student_homework 1",
    "lesson": 1,
    "student": 1
  },
  {
    "id": 2,
    "grade": {
      "id": 2,
      "teacher_last_name": "Test teacher_last_name 2",
      "status": "done",
      "grade": "test grade 2",
    },
    "student_first_name": "Student 2",
    "student_last_name": "",
    "student_homework": "student_homework 2",
    "lesson": 1,
    "student": 2
  }
];


describe('StudentsHomework', () => {
  it('render correctly StudentsHomework component', () => {
    const tree = renderer.create(<TestStudentsHomework homework={homework} />).toJSON();
    expect(tree).toMatchSnapshot()
  });

  it('render StudentsHomework correctly with given props', () => {
    const { queryByText } = render(<TestStudentsHomework homework={homework} />);
    expect(queryByText(/Student 1/i)).toBeTruthy();
    expect(queryByText(/Student 2/i)).toBeTruthy();
  });

});