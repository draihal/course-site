describe('The Profile Page', function () {

  it('logs in programmatically without using the UI', function () {
    const email = 'studenttest1@dot.com';
    const password = '+79271111133';

    // DON'T WORK
    // programmatically log us in without needing the UI
    // cy.request('POST', '/signin', {
    //   email: email,
    //   password: password
    // });
    // -OR-, with visit the same problem
    // cy.request({
    //   method: 'POST',
    //   url: '/signin',
    //   form: true,
    //   body: {
    //     email,
    //     password
    //   }
    // });
    // now that we're logged in, we can visit
    // any kind of restricted route!
    // cy.visit('/profile');

    cy.visit('/signin');
    cy.get('input[name=email]').type(email);
    cy.get('input[name=password]').type(`${password}{enter}`);
    cy.url().should('include', '/profile');

    // our auth cookie should be present
    cy.getCookie('token').should('exist');

    cy.get('h2').should('contain', 'Мой профиль');
    cy.get('img').should('have.length', 1);
    cy.get('#image').should('have.length', 1);
    cy.get('.text-center > form > .btn').contains('Изменить');

    cy.get('input[name=first_name]').should('have.length', 1);
    cy.get('input[name=last_name]').should('have.length', 1);
    cy.get('input[name=email]').should('have.length', 1);
    cy.get('input[name=phone_number]').should('have.length', 1);
    cy.get(':nth-child(2) > [type="submit"]').should('have.length', 1);
    cy.get('.btn-email').should('have.length', 1);
    cy.get('.btn-password').should('have.length', 1);

    cy.get('.col-md-9 > :nth-child(4)').contains('Дополнительная информация');


  })

});
