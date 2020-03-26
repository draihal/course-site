import React from 'react'
import renderer from 'react-test-renderer'
import { fireEvent, render } from '@testing-library/react'
import TestAddGrade from './AddGrade'

const homework = {
  'id': 1,
  'lesson': 111,
  'student': 11,
  'student_first_name': 'Testing First Name',
  'student_last_name': 'Testing Last Name',
  'student_homework': 'Testing Homework'
};


describe('AddGrade', () => {
  it('render correctly AddGrade component', () => {
    const tree = renderer.create(<TestAddGrade teacherId={'13'} homework={homework} token={null} />).toJSON();
    expect(tree).toMatchSnapshot()
  });

  it('render AddGrade correctly with given props', () => {
    const { queryByText } = render(<TestAddGrade teacherId={'13'} homework={homework} token={null} />);
    expect(queryByText(/Testing First Name/i)).toBeTruthy();
  });

  it('inputs changes', () => {
    const { getByText, getByLabelText } = render(
      <TestAddGrade teacherId={'13'} homework={homework} token={null} />
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