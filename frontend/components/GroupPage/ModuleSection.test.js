import React from 'react'
import renderer from 'react-test-renderer'
import { render } from '@testing-library/react'
import TestModuleSection from './ModuleSection'

const modules = [
  {
    "id": 1,
    "lessons": [],
    "name": "1 месяц",
  },
  {
    "id": 2,
    "lessons": [],
    "name": "2 месяц",
  },
  {
    "id": 3,
    "lessons": [],
    "name": "3 месяц",
  }
];



describe('ModuleSection', () => {
  it('render correctly ModuleSection component', () => {
    const tree = renderer.create(<TestModuleSection modules={modules} />).toJSON();
    expect(tree).toMatchSnapshot()
  });

  it('render ModuleSection correctly with given props', () => {
    const { queryByText } = render(<TestModuleSection modules={modules} />);
    expect(queryByText(/1 месяц/i)).toBeTruthy();
    expect(queryByText(/2 месяц/i)).toBeTruthy();
    expect(queryByText(/3 месяц/i)).toBeTruthy();
  });

});