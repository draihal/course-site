import React from 'react'
import renderer from 'react-test-renderer'
import { render } from '@testing-library/react'
import TestStudentCourses from './StudentCourses'

const groups = [
  {
    "id": 1,
    "url": "http://127.0.0.1:8000/api/v1/education/groups/pyweb-2019-09-16/",
    "name": "PyWeb-2019-09-16",
    "slug": "pyweb-2019-09-16"
  }
];


describe('StudentCourses', () => {
  it('render correctly StudentCourses component', () => {
    const tree = renderer.create(<TestStudentCourses groups={groups} />).toJSON();
    expect(tree).toMatchSnapshot()
  });

  it('render StudentCourses correctly with given props', () => {
    const { queryByText } = render(<TestStudentCourses groups={groups} />);
    expect(queryByText(/PyWeb-2019-09-16/i)).toBeTruthy();
  });

});