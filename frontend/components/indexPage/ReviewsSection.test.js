import React from 'react'
import renderer from 'react-test-renderer'
import { render } from '@testing-library/react'
import TestReviewsSection from './ReviewsSection'

const reviews = [
  {
    "id": 2,
    "url": "/api/v1/pages/reviews/2/",
    "user_id": 2,
    "student_first_name": "Student2",
    "student_last_name": "Test2",
    "student_image": null,
    "text": "Тестовый отзыв 2"
  },
  {
    "id": 1,
    "url": "/api/v1/pages/reviews/1/",
    "user_id": 1,
    "student_first_name": "Student1",
    "student_last_name": "Test1",
    "student_image": null,
    "text": "Тестовый отзыв 1"
  }
];


describe('ReviewsSection', () => {
  it('render correctly ReviewsSection component', () => {
    const tree = renderer.create(<TestReviewsSection reviews={reviews} />).toJSON();
    expect(tree).toMatchSnapshot()
  });

  it('render ReviewsSection correctly with given props', () => {
    const { queryByText } = render(<TestReviewsSection reviews={reviews} />);
    expect(queryByText('Тестовый отзыв 2')).toBeTruthy();
    expect(queryByText('Тестовый отзыв 1')).toBeTruthy();
  });

});