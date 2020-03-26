import React from 'react'
import renderer from 'react-test-renderer'
import { render } from '@testing-library/react'
import TestLessonSection from './LessonSection'

const lessons = [
  {
    "id": 1,
    "name": "lessontest",
    "slug": "lessontest",
    "number": 1,
    "description": "lessontest description",
    "poll_url": "http://test.com/",
    "datetime": "2020-02-10T20:00:05+03:00",
    "url_translation": "http://127.0.0.1:8000/",
    "homework_title": "lessontest homework_title",
    "homework_description": "lessontest homework_description",
    "homework_date": "2020-02-12",
    "module": 1,
    "group": 1
  }
];


describe('LessonSection', () => {
  it('render correctly LessonSection component', () => {
    const tree = renderer.create(<TestLessonSection lessons={lessons} />).toJSON();
    expect(tree).toMatchSnapshot()
  });

  it('render LessonSection correctly with given props', () => {
    const { queryByText } = render(<TestLessonSection lessons={lessons} />);
    expect(queryByText(/lessontest description/i)).toBeTruthy();
  });

});