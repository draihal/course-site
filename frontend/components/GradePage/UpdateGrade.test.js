import React from 'react'
import renderer from 'react-test-renderer'
import { fireEvent, render } from '@testing-library/react'
import TestUpdateGrade from './UpdateGrade'

const homework = {
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


describe('UpdateGrade', () => {
  it('render correctly UpdateGrade component', () => {
    const tree = renderer.create(
      <TestUpdateGrade teacherId={'13'} homework={homework} token={null} grade={homework.grade} />
    ).toJSON();
    expect(tree).toMatchSnapshot()
  });

  it('render UpdateGrade correctly with given props', () => {
    const { queryByText } = render(
      <TestUpdateGrade teacherId={'13'} homework={homework} token={null} grade={homework.grade} />
    );
    expect(queryByText(/Testing First Name/i)).toBeTruthy();
  });

  it('inputs changes', () => {
    const { getByText, getByLabelText } = render(
      <TestUpdateGrade teacherId={'13'} homework={homework} token={null} grade={homework.grade} />
    );
    fireEvent.change(getByLabelText('Оценка'), {
      target: { value: 'Input has changed' }
    });
    fireEvent.change(getByLabelText('Статус проверки'), {
      target: { value: 'done' }
    });
    expect(getByText('Input has changed')).toBeInTheDocument();
    expect(getByText('Сдано')).toBeInTheDocument();
  });

});