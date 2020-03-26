import React from 'react'
import renderer from 'react-test-renderer'
import { render } from '@testing-library/react'
import TestNavbar from './Navbar'


describe('Navbar', () => {
  it('render correctly Navbar component', () => {
    const tree = renderer.create(<TestNavbar />).toJSON();
    expect(tree).toMatchSnapshot()
  });

  it('render Navbar correctly with isAuthenticated=false', () => {
    const { queryByTestId } = render(<TestNavbar isAuthenticated={false} />);
    expect(queryByTestId('signin-link')).toBeTruthy();
    expect(queryByTestId('profile-link')).toBeFalsy();
    expect(queryByTestId('my-courses-link')).toBeFalsy();
    // expect(queryByTestId('bell-link')).toBeFalsy();
    expect(queryByTestId('deauthenticate-link')).toBeFalsy();
  });

    it('render Navbar correctly with isAuthenticated=true', () => {
    const { queryByTestId } = render(<TestNavbar isAuthenticated={true} />);
    expect(queryByTestId('signin-link')).toBeFalsy();
    expect(queryByTestId('profile-link')).toBeTruthy();
    expect(queryByTestId('my-courses-link')).toBeTruthy();
    // expect(queryByTestId('bell-link')).toBeTruthy();
    expect(queryByTestId('deauthenticate-link')).toBeTruthy();
  });

});