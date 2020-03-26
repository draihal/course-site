import React from 'react'
import renderer from 'react-test-renderer'
import { fireEvent, render } from '@testing-library/react'
import TestGradeSection from './GradeSection'

const homework1 = {
  'id': 1,
  'lesson': 111,
  'student': 11,
  'student_first_name': 'Testing First Name',
  'student_last_name': 'Testing Last Name',
  'student_homework': 'Testing Homework',
  'grade': {
    'status': 'rework',
    'grade': 'Test grade',
    'lesson': 2,
    'id': 1,
    'student': 22
  }
};

const homework2 = {
  'id': 1,
  'lesson': 111,
  'student': 11,
  'student_first_name': 'Testing First Name 2',
  'student_last_name': 'Testing Last Name',
  'student_homework': 'Testing Homework',
  'grade': []
};


describe('GradeSection', () => {
  it('render correctly GradeSection component', () => {
    const tree = renderer.create(
      <TestGradeSection teacherId={'13'} homework={homework1} token={null} />
    ).toJSON();
    expect(tree).toMatchSnapshot()
  });

  it('render GradeSection correctly with given props with grade', () => {
    const { queryByText } = render(
      <TestGradeSection teacherId={'13'} homework={homework1} token={null} />
    );
    expect(queryByText(/Testing First Name/i)).toBeTruthy();
    expect(queryByText(/Test grade/i)).toBeTruthy();
  });

  it('render GradeSection correctly with given props without grade', () => {
    const { queryByText } = render(
      <TestGradeSection teacherId={'13'} homework={homework2} token={null} />
    );
    expect(queryByText(/Testing First Name 2/i)).toBeTruthy();
    expect(queryByText(/Test grade/i)).toBeFalsy();
  });

});