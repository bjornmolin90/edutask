describe('Logging into the system', () => {
  // define variables that we need on multiple occasions
  let uid // user id
  let name // name of the user (firstName + ' ' + lastName)
  let email // email of the user

  before(function () {
    // create a fabricated user from a fixture
    cy.fixture('user.json')
      .then((user) => {
        cy.request({
          method: 'POST',
          url: 'http://localhost:5000/users/create',
          form: true,
          body: user
        }).then((response) => {
          uid = response.body._id.$oid
          name = user.firstName + ' ' + user.lastName
          email = user.email
        })
      })
  })

  before(function () {
    cy.visit('http://localhost:3000')
    cy.get('.inputwrapper #email')
    .type(email)
    cy.get('form')
    .submit()
    cy.get('.inputwrapper #title')
    .type("test")
    cy.get('.inputwrapper #url')
    .type("blabla")
    cy.get('form')
    .submit()
    cy.contains('test')
    .click()
  })

  beforeEach(function () {
    // enter the main main page
    cy.visit('http://localhost:3000')
    cy.get('.inputwrapper #email')
    .type(email)
    cy.get('form')
    .submit()
    cy.contains('test')
    .click()
  })

  it('add a todo item', () => {
    // make sure the landing page contains a header with "login"
    cy.get(".inline-form")
      .type('todo_test')
      .submit()
    cy.get('.todo-item')
    .should('contain.text', 'todo_test')
  })

  it('check if add button is disabled when no text in input field', () => {
    // check if add button is disabled"
    cy.get(".inline-form")
    .find('input[type=submit]')
    .should('be.disabled')
  })

  it('check that item is checked after click', () => {
    // check if add button is disabled"
    cy.get(".checker")
    .eq(1)
    .click()
    .should('have.class', 'checked')
  })

  it('check that item is unchecked after click when it came from a checked state', () => {
    // check if add button is disabled"
    cy.get(".checker")
    .eq(1)
    .click()
    .should('have.class', 'unchecked')
  })

  it('Remove todo item', () => {
    cy.contains('.todo-item', 'todo_test')
        .find('span.remover')
        .click()
    cy.contains('.todo-item', 'todo_test')
        .should('not.exist')
})

  after(function () {
    // clean up by deleting the user from the database
    cy.request({
      method: 'DELETE',
      url: `http://localhost:5000/users/${uid}`
    }).then((response) => {
      cy.log(response.body)
    })
  })
})