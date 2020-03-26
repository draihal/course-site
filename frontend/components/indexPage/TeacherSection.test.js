import React from 'react'
import renderer from 'react-test-renderer'
import { render } from '@testing-library/react'
import TestTeacherSection from './TeacherSection'

const teachers = [
  {
    "teacher_id": 1,
    "url": "/api/v1/profile/teacher/1/",
    "avatar": null,
    "teacher_first_name": "Teacher 1",
    "teacher_last_name": "Test 1",
    "company": "",
    "position": "",
    "bio": ""
  },
  {
    "teacher_id": 2,
    "url": "/api/v1/profile/teacher/2/",
    "avatar":  null,
    "teacher_first_name": "Teacher 2",
    "teacher_last_name": "Test 2",
    "company": "",
    "position": "",
    "bio": "Testing bio 2"
  },
  {
    "teacher_id": 3,
    "url": "/api/v1/profile/teacher/3/",
    "avatar": null,
    "teacher_first_name": "Teacher 3",
    "teacher_last_name": "Test 3",
    "company": "",
    "position": "",
    "bio": "Testing bio 3"
  }
];


describe('TeacherSection', () => {
  it('render correctly TeacherSection component', () => {
    const tree = renderer.create(<TestTeacherSection teachers={teachers} />).toJSON();
    expect(tree).toMatchSnapshot()
  });

  it('render TeacherSection correctly with given props', () => {
    const { queryByText } = render(<TestTeacherSection teachers={teachers} />);
    expect(queryByText(/Teacher 1/i)).toBeTruthy();
    expect(queryByText(/Teacher 2/i)).toBeTruthy();
    expect(queryByText(/Teacher 3/i)).toBeTruthy();
  });

});