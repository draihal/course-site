describe('The SignIn Page', function () {
  it('sets auth cookie when logging in via form submission', function () {
    const email = 'studenttest1@dot.com';
    const password = '+79271111133';

    cy.visit('/signin');

    // SignIn page form and buttons
    cy.get('.h3').contains('Вход');
    cy.get('input[name=email]').should('have.length', 1);
    cy.get('input[name=password]').should('have.length', 1);
    cy.get('[type="submit"]').should('have.length', 1);
    cy.get('.mt-5').contains('Еще не зарегистрированы?');
    cy.get('[type="registration"]').should('have.length', 1);


    cy.get('input[name=email]').type(email);

    // {enter} causes the form to submit
    cy.get('input[name=password]').type(`${password}{enter}`);

    // we should be redirected to /profile
    cy.url().should('include', '/profile');

    // our auth cookie should be present
    cy.getCookie('token').should('exist');

    // UI should reflect this user being logged in
    cy.get('h2').should('contain', 'Мой профиль');

    // Log out
    cy.get('[data-testid=deauthenticate-link] > .svg-inline--fa').click();
    cy.url().should('include', '/')
  })
});
