import UserCard from "./UserCard";

const testUser = {
  name: "test username",
  age: 20,
  gender: "male",
  bio: "test bio",
};

describe("UserCard", () => {
  it("renders UserCard with correct user's data", () => {
    cy.mount(<UserCard user={testUser} />);
    cy.get('[data-cy="test-UserName-and-age"]').should(
      "contain.text",
      "test username | 20",
    );
  });
});
