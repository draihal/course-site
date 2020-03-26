import React from 'react'
import renderer from 'react-test-renderer'
import { render } from '@testing-library/react'
import TestTeacherGroups from './TeacherGroups'

const groups = [
  {
    "id": 1,
    "url": "http://127.0.0.1:8000/api/v1/education/groups/pyweb-2019-09-16/",
    "name": "PyWeb-2019-09-16",
    "slug": "pyweb-2019-09-16"
  }
];


describe('TeacherGroups', () => {
  it('render correctly TeacherGroups component', () => {
    const tree = renderer.create(<TestTeacherGroups groups={groups} />).toJSON();
    expect(tree).toMatchSnapshot()
  });

  it('render TeacherGroups correctly with given props', () => {
    const { queryByText } = render(<TestTeacherGroups groups={groups} />);
    expect(queryByText(/PyWeb-2019-09-16/i)).toBeTruthy();
  });

});