import React from 'react'
import renderer from 'react-test-renderer'
import { render } from '@testing-library/react'
import TestCoursesSection from './CoursesSection'


describe('CoursesSection', () => {
  it('render correctly CoursesSection component', () => {
    const tree = renderer.create(<TestCoursesSection
      description={'Тестовое описание'}
      number_of_students={111}
      number_of_groups={11}
      number_of_teachers={11}
    />).toJSON();
    expect(tree).toMatchSnapshot()
  });

  it('render CoursesSection correctly with given props', () => {
    const { queryByText } = render(<TestCoursesSection
      description={'Тестовое описание'}
      number_of_students={111}
      number_of_groups={11}
      number_of_teachers={11}
    />);
    expect(queryByText('Тестовое описание')).toBeTruthy();
    expect(queryByText('111 студентов')).toBeTruthy();
    expect(queryByText('11 групп')).toBeTruthy();
    expect(queryByText('11 преподавателей')).toBeTruthy();
  });

});