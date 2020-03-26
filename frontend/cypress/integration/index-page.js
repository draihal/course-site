describe("Index page", () => {
  /*
  * Visits the page before each test
  */
  beforeEach(() => {
    cy.log(`Visiting http://localhost:3000`);
    cy.visit('/');
  });

  /*
  * Header section
  */
  it('clicking "navbar-brand" navigates to a / url', function() {
    cy.contains('Онлайн курсы').click();
    cy.url().should('include', '/')
  });
  it('clicking "Главная" navigates to a /#home url', function() {
    cy.contains('Главная').click();
    cy.url().should('include', '/#home')
  });
  it('clicking SignIn navigates to a /signin url', function() {
    cy.get('[data-testid=signin-link] > .svg-inline--fa').click();
    cy.url().should('include', '/signin')
  });

  /*
  * HomeSection
  */
  it('HomeSection should have a title, description and a button', function() {
    cy.get('.container > h1').contains('Онлайн курсы');
    cy.get('.container > h3').contains('Онлайн образование для всех');
    cy.get('.container > .btn').should('have.length', 1);
  });

  /*
  * CoursesSection
  */
  it('CoursesSection should have a title, description and a button', function() {
    cy.get('.col-12 > h1').contains('Курсы');
    cy.get(':nth-child(1) > .col-12 > .lead').should('have.length', 1);
    cy.get(':nth-child(1) > .col-12 > .btn').should('have.length', 1);
  });
  it('CoursesSection should have a title of statistic and three feature divs', function() {
    cy.get('.jumbotron > .container > .narrow > .col-12 > .heading')
      .contains('Наша статистика');
    cy.get('.jumbotron > .container > .narrow > .row > .col-md-4 > .feature')
      .should('have.length', 3);
  });

  /*
  * TeacherSection
  */
  it('TeacherSection should have a title, three teachers and button', function() {
    cy.get('.dark > .container > .narrow > .col-12 > .heading')
      .contains('Преподаватели');
    cy.get('.dark > .container > .row > .teachers')
      .should('have.length', 3);
    cy.get(':nth-child(3) > .col-12 > .btn').should('have.length', 1);
  });

  /*
  * ReviewsSection
  */
  it('ReviewsSection should have a title, two reviews and button', function() {
    cy.get('.container > .col-12 > .heading')
      .contains('Отзывы');
    cy.get('.jumbotron > .container > .row > .reviews')
      .should('have.length', 2);
    cy.get('#reviews > .narrow > .btn').should('have.length', 1);
  });

  /*
  * Footer section
  */
  it("Footer section should have 4 column", () => {
    cy.get('#sticky-footer > .row > .footer-column')
      .should("have.length", 4);
  });
});

