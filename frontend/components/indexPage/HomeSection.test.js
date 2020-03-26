import React from 'react'
import renderer from 'react-test-renderer'
import { render } from '@testing-library/react'
import TestHomeSection from './HomeSection'


describe('HomeSection', () => {
  it('render correctly HomeSection component', () => {
    const tree = renderer.create(<TestHomeSection
      title={'Тестовый title'}
      short_description={'Тестовое описание'}
    />).toJSON();
    expect(tree).toMatchSnapshot()
  });

  it('render HomeSection correctly with given props', () => {
    const { queryByText } = render(<TestHomeSection
      title={'Тестовый title'}
      short_description={'Тестовое описание'}
    />);
    expect(queryByText('Тестовый title')).toBeTruthy();
    expect(queryByText('Тестовое описание')).toBeTruthy();
  });

});